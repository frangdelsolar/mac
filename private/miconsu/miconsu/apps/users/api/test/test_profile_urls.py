from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from client.api.views import ClientViewSet
from client.models import Client, ClientPlan, ClientType
from django.contrib.auth import get_user_model 
from users.enum import UserRoles
from users.models import Profile
from collections import OrderedDict


User = get_user_model()

class URLTest(APITestCase):
    fixtures = ['clients.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.get_request = self.factory.get("")
        self.post_request = self.factory.post("", {}, format="json")
        self.put_request = self.factory.put("", {}, format="json")
        self.delete_request = self.factory.delete("")

        self.list_view = ClientViewSet.as_view({'get': 'list'})
        self.create_view = ClientViewSet.as_view({'post': 'create'})
        self.detail_view = ClientViewSet.as_view({'get': 'retrieve'})
        self.update_view = ClientViewSet.as_view({'put': 'update'})
        self.delete_view = ClientViewSet.as_view({'delete': 'destroy'})

        self.professional_user = User.objects.get(username="Professional")
        self.no_profile_user = User.objects.get(username='NoProfileUser')
        self.no_client_profile = User.objects.get(username='NoClientProfileUser')
        self.app_admin = User.objects.get(username='AppAdmin')

