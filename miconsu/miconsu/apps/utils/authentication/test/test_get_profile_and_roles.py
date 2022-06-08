from rest_framework.test import APITestCase
from rest_framework.test import  APIRequestFactory
from django.contrib.auth import get_user_model 
from utils.authentication.get_profile_and_roles import get_profile_and_roles
from users.models import Profile
from users.enum import UserRoles

User = get_user_model()

class URLTest(APITestCase):
    fixtures = ['clients.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.get_request = self.factory.get("")
        self.professional_user = User.objects.get(username='Professional')

    def test_get_profile_and_roles(self):
        """Function should return user profile and roles from request"""
        self.get_request.user = self.professional_user
        profile, roles = get_profile_and_roles(self.get_request)
        self.assertEqual(profile, Profile.get_by_user(self.professional_user))
        self.assertEqual(roles, [UserRoles.PROFESSIONAL.value])

