from django.test import TestCase
from client.models import ClientPlan
from client.api.serializers import ClientPlanSerializer


class ClientPlanSerializerTestCase(TestCase):
    def setUp(self):
        self.plan_nuevo = ClientPlan.objects.create(name="Plan Nuevo")
        self.plan_viejo = ClientPlan.objects.create(name="Plan Viejo")

    def test_client_plan_get_item(self):
        """Get Item Client Plan"""
        serializer = ClientPlanSerializer(self.plan_nuevo)
        self.assertEqual(serializer.data, {'id': 1, 'name': 'Plan Nuevo'})

    def test_client_plan_get_items(self):
        """Get Items Client Plan"""
        instances = ClientPlan.objects.all()
        serializer = ClientPlanSerializer(instances, many=True)
        self.assertEqual(len(serializer.data), 2)

    def test_client_plan_post(self):
        """Post Item Client Plan"""
        data = {
            'name': 'Tercer Plan'
        }
        serializer = ClientPlanSerializer(data=data)
        serializer.is_valid()
        instance = serializer.save()
        self.assertEqual(instance.name, data['name'])