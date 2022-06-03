from django.test import TestCase
from client.models import ClientPlan


class ClientPlanTestCase(TestCase):
    def setUp(self):
        ClientPlan.objects.create(name="Plan Nuevo")

    def test_client_plan_init(self):
        """Client Plan is created"""
        ct = ClientPlan.objects.filter(name="Plan Nuevo")

        self.assertEqual(ct.count(), 1)

    def test_client_plan_str(self):
        """Client Plan String"""
        cp = ClientPlan.objects.get(name="Plan Nuevo")

        self.assertEqual(cp.__str__(), "Plan Nuevo")