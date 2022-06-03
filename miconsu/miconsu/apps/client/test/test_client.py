from django.test import TestCase
from client.models import ClientType, ClientPlan, Client
from django.contrib.auth import get_user_model

User = get_user_model()

class ClientTestCase(TestCase):
    def setUp(self):
        admin = User.objects.create(username="pepe", password="1234")
        ct = ClientType.objects.create(name="Professional")
        cp = ClientPlan.objects.create(name="Plan Nuevo")
        Client.objects.create(
            name="Pedro",
            administrator=admin,
            client_plan=cp,
            client_type=ct
        )

    def test_client_init(self):
        """Client is created"""
        c= Client.objects.get(name="Pedro")

        self.assertEqual(c.administrator.username, "pepe")
        self.assertEqual(c.client_type.name, "Professional")
        self.assertEqual(c.client_plan.name, "Plan Nuevo")

    def test_client_str(self):
        """Client String"""
        c= Client.objects.get(name="Pedro")

        self.assertEqual(c.__str__(), "Pedro")