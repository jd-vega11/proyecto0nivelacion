from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from events.models import Events
from events.serializers import EventsSerializer, UsersSerializer
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
def users_create(request):
    if request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UsersSerializer(data=users_data)
        if users_serializer.is_valid():
            try:
                User.objects.create_user(
                username= users_serializer.data['username'],
                password=users_serializer.data['password'],
                email=users_serializer.data['email'],
                first_name=users_serializer.data['first_name'],
                last_name=users_serializer.data['last_name']
                )

                return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                if e.__cause__.pgcode == '23505':
                    return JsonResponse({'message':'The user already exists'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return JsonResponse({'message':'It was no possible to create the user. Check the fields and try again'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def events_list(request):
    if request.method == 'GET':
        events = Events.objects.filter(user=request.user.id)
        events_serializer = EventsSerializer(events, many = True)
        return JsonResponse(events_serializer.data, safe=False)
    elif request.method == 'POST':
        events_data = JSONParser().parse(request)
        events_data['user'] = request.user.id
        events_serializer = EventsSerializer(data=events_data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse(events_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(events_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def event_detail(request, event_uuid):
    #permission_classes = (IsAuthenticated,)
    try:
        user_event = Events.objects.get(event_uuid = event_uuid, user=request.user.id)
    except ObjectDoesNotExist as dne:
        return JsonResponse({'message':'The event does not exist or you dont have the necessary permissions'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'message':'We couldnt process the request, please try again'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if request.method == 'GET':
        events_serializer = EventsSerializer(user_event)
        return JsonResponse(events_serializer.data)
    elif request.method == 'PUT':
        events_data = JSONParser().parse(request)
        events_serializer = EventsSerializer(user_event, data=events_data)
        if events_serializer.is_valid():
            events_serializer.save()
            return JsonResponse(events_serializer.data)
        return JsonResponse(events_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user_event.delete()
        return JsonResponse({'message':'Event was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
