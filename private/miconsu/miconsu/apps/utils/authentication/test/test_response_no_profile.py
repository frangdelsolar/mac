from rest_framework.test import APITestCase
from rest_framework.test import  APIRequestFactory, force_authenticate
from client.api.views import ClientViewSet
from django.contrib.auth import get_user_model 
from utils.authentication.response_no_profile import response_no_profile


User = get_user_model()

class URLTest(APITestCase):
    fixtures = ['clients.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.get_request = self.factory.get("")
        self.no_profile_user = User.objects.get(username='NoProfileUser')

    def test_view__500__no_profile(self):
        """View should return Error if user has no profile"""
        self.get_request.user = self.no_profile_user
        response = response_no_profile(self.get_request)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, {'Error': 'El usuario no tiene un perfil configurado'})

