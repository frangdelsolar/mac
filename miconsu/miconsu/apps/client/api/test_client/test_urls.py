from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.reverse import reverse
from client.api.views import ClientViewSet
from client.models import Client, ClientPlan, ClientType
from django.contrib.auth import get_user_model 
User = get_user_model()



class URLTest(TestCase):
    def setUp(self):
        self.user_one = User.objects.create(
            username="pepito",
            first_name="Pepe",
            last_name="Honguito",
            email="pepe@honguito.com"
        )
        self.cp = ClientPlan.objects.create(name="Plan Nuevo")
        self.ct = ClientType.objects.create(name="Professional")
        self.client_one = Client.objects.create(
            name="Cliente 1",
            administrator=self.user_one,
            client_plan=self.cp,
            client_type=self.ct
        )

        self.client_two = Client.objects.create(
            name="Cliente 2",
            administrator=self.user_one,
            client_plan=self.cp,
            client_type=self.ct
        )

    def test_url_returns_200(self):
        api_request = APIRequestFactory().get("")
        detail_view = ClientViewSet.as_view({'get': 'retrieve'})
        response = detail_view(api_request, pk=self.client_one.id)
        self.assertEqual(response.status_code, 200)