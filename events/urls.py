from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from events import views

urlpatterns = [
    url(r'^api/events$', views.events_list),
    url(r'^api/events/(?P<event_uuid>\s*([a-f0-9\\-]*){1}\s*)$', views.event_detail),
    url(r'^api/create-user$', views.users_create),
    path('api/api-auth', obtain_auth_token, name='api-auth')

]
