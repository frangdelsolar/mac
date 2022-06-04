from django.test import TestCase
from client.models import ClientType, ClientPlan, Client
from django.contrib.auth import get_user_model

User = get_user_model()

class ClientTestCase(TestCase):
    def setUp(self):
        self.admin = User.objects.create(username="pepe", password="1234")
        self.ct = ClientType.objects.create(name="Professional")
        self.cp = ClientPlan.objects.create(name="Plan Nuevo")
        self.client = Client.objects.create(
            name="Pedro",
            administrator=self.admin,
            client_plan=self.cp,
            client_type=self.ct
        )

    def test_client_init(self):
        """Client is created"""
        self.assertEqual(self.client.administrator, self.admin)
        self.assertEqual(self.client.client_type, self.ct)
        self.assertEqual(self.client.client_plan, self.cp)

    def test_client_str(self):
        """Client String"""
        self.assertEqual(self.client.__str__(), "Pedro")