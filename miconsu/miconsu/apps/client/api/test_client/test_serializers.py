from django.test import TestCase
from client.models import ClientType, ClientPlan, Client
from client.api.serializers import ClientSerializer, ClientPlanSerializer, ClientTypeSerializer
from django.contrib.auth import get_user_model
from collections import OrderedDict


User = get_user_model()

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
        self.assertEqual(serializer.data, {'id': 1, 'name': 'Cliente 1', 'administrator': OrderedDict([('id', 1), ('username', 'pepito'), ('first_name', 'Pepe'), ('last_name', 'Honguito'), ('email', 'pepe@honguito.com')]), 'client_plan': OrderedDict([('id', 1), ('name', 'Plan Nuevo')]), 'client_type': OrderedDict([('id', 1), ('name', 'Professional')])})

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
                'username': 'pepitohonguito'
            },
            'client_type': {
                'name': 'Otro Tipo'
            },
            'client_plan':{
                'name': "Plan Nuevo"
            }
        }
        serializer = ClientSerializer(data=data)
        serializer.is_valid()
        instance = serializer.save()
        self.assertEqual(instance.name, data['name'])
        self.assertEqual(instance.administrator.username, 'pepitohonguito')
        self.assertEqual(instance.client_type.name, 'Otro Tipo')
        self.assertEqual(instance.client_plan.name, 'Plan Nuevo')