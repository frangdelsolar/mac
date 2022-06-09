from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from client.api.views import ClientViewSet


class URLTest(APITestCase):
    fixtures = ['clients.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.get_request = self.factory.get("")
        self.list_view = ClientViewSet.as_view({'get': 'list'})

    def test_view__403__anonymous__not_authenticated(self):
        """View should return Forbidden if user is not authenticated"""
        response = self.list_view(self.get_request)
        self.assertEqual(response.status_code, 403)



