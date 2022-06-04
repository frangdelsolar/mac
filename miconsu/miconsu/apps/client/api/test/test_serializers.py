from django.test import TestCase
from client.models import ClientType, ClientPlan, Client
from client.api.serializers import ClientPlanSerializer, ClientTypeSerializer, ClientSerializer
from users.api.serializers import UserSerializer
from django.contrib.auth import get_user_model
from collections import OrderedDict


User = get_user_model()

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


class ClientTypeSerializerTestCase(TestCase):
    def setUp(self):
        self.professional_ct = ClientType.objects.create(name="Professional")
        self.organization_ct = ClientType.objects.create(name="Organization")

    def test_client_type_get_item(self):
        """Get Item Client Type"""
        serializer = ClientTypeSerializer(self.professional_ct)
        self.assertEqual(serializer.data, {'id': 1, 'name': 'Professional'})

    def test_client_type_get_items(self):
        """Get Items Client Type"""
        instances = ClientType.objects.all()
        serializer = ClientTypeSerializer(instances, many=True)
        self.assertEqual(len(serializer.data), 2)

    def test_client_type_save(self):
        """Post Item Client Type"""
        data = {
            'name': 'Gran Empresa'
        }
        serializer = ClientPlanSerializer(data=data)
        serializer.is_valid()
        instance = serializer.save()
        self.assertEqual(instance.name, data['name'])


class ClientSerializerTestCase(TestCase):
    def setUp(self):
        self.admin = User.objects.create(
            username="pepito",
            first_name="Pepe",
            last_name="Honguito",
            email="pepe@honguito.com"
        )
        self.cp = ClientPlan.objects.create(name="Plan Nuevo")
        self.ct = ClientType.objects.create(name="Professional")
        self.client_one = Client.objects.create(
            name="Cliente 1",
            administrator=self.admin,
            client_plan=self.cp,
            client_type=self.ct
        )

        self.client_two = Client.objects.create(
            name="Cliente 2",
            administrator=self.admin,
            client_plan=self.cp,
            client_type=self.ct
        )

    def test_client_get_item(self):
        """Get Item Client"""
        serializer = ClientSerializer(self.client_one)
        self.assertEqual(serializer.data, {'id': 1, 'name': 'Cliente 1', 'administrator': OrderedDict([('id', 1), ('username', 'pepito'), ('first_name', 'Pepe'), ('last_name', 'Honguito'), ('email', 'pepe@honguito.com'), ('roles', [])]), 'client_plan': OrderedDict([('id', 1), ('name', 'Plan Nuevo')]), 'client_type': OrderedDict([('id', 1), ('name', 'Professional')])})

    def test_client_get_items(self):
        """Get Items Client"""
        instances = Client.objects.all()
        serializer = ClientSerializer(instances, many=True)
        self.assertEqual(len(serializer.data), 2)

    def test_client_save(self):
        """Post Item Client"""
        data = {
            'name': 'Nuevo Cliente',
            'administrator': {
                'username': 'pepito'
            },
            'client_type': {
                'name': 'Professional'
            },
            'client_plan':{
                'name': 'Plan Nuevo'
            }
        }

        serializer = ClientPlanSerializer(data=data)
        serializer.is_valid()
        instance = serializer.save()
        self.assertEqual(instance.name, data['name'])