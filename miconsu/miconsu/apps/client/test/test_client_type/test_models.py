from django.test import TestCase
from client.models import ClientType


class ClientTypeTestCase(TestCase):
    def setUp(self):
        self.ct = ClientType.objects.create(name="Professional")

    def test_client_type_init(self):
        """Client Type is created"""
        self.assertEqual(self.ct.name, 'Professional')

    def test_client_type_str(self):
        """Client Type String"""
        self.assertEqual(self.ct.__str__(), "Professional")