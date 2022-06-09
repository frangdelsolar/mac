from rest_framework.test import APITestCase
from rest_framework.test import  APIRequestFactory, force_authenticate
from client.api.views import ClientViewSet
from django.contrib.auth import get_user_model 
from utils.authentication.response_no_client_and_not_app_admin import response_no_client_and_not_app_admin


User = get_user_model()

class URLTest(APITestCase):
    fixtures = ['clients.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.get_request = self.factory.get("")
        self.no_client_profile = User.objects.get(username='NoClientProfileUser')


    def test_view__500__no_profile(self):
        """View should return Error if profile has no client"""
        self.get_request.user = self.no_client_profile
        response = response_no_client_and_not_app_admin(self.get_request)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, {'Error': 'El perfil de usuario no tiene un cliente configurado'})

