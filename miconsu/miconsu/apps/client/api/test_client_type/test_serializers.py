from django.test import TestCase
from client.models import ClientType
from client.api.serializers import ClientTypeSerializer


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
        serializer = ClientTypeSerializer(data=data)
        serializer.is_valid()
        instance = serializer.save()
        self.assertEqual(instance.name, data['name'])