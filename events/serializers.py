from rest_framework import serializers
from events.models import Events
from django.contrib.auth.models import User

class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ['event_uuid', 'event_name', 'event_category', 'event_place', 'event_address', 'event_initial_date',
        'event_final_date', 'event_type', 'thumbnail', 'user']

    def to_representation(self, obj):
        # get the original representation
        event = super(EventsSerializer, self).to_representation(obj)

        # remove 'user' field
        event.pop('user')
        return event

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
