from django.test import TestCase
from client.models import ClientType


class ClientTypeTestCase(TestCase):
    def setUp(self):
        ClientType.objects.create(name="Professional")

    def test_client_type_init(self):
        """Client Type is created"""
        ct = ClientType.objects.filter(name="Professional")

        self.assertEqual(ct.count(), 1)