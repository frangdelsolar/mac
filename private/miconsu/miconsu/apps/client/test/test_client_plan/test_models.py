from django.test import TestCase
from client.models import ClientPlan


class ClientPlanTestCase(TestCase):
    def setUp(self):
        self.cp = ClientPlan.objects.create(name="Plan Nuevo")

    def test_client_plan_init(self):
        """Client Plan is created"""
        self.assertEqual(self.cp.name, 'Plan Nuevo')

    def test_client_plan_str(self):
        """Client Plan String"""
        self.assertEqual(self.cp.__str__(), "Plan Nuevo")