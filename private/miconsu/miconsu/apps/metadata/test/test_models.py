from django.test import TestCase
from metadata.models import Metadata
from django.contrib.auth import get_user_model

User = get_user_model()

class MetadataTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="pepe", password="1234")
        self.metadata = Metadata.objects.create(created_by=self.user, updated_by=self.user)

    def test_metadata_init(self):
        """Metadata adds timestamp and user"""
        self.assertEqual(self.metadata.created_by, self.user)
        self.assertEqual(self.metadata.updated_by, self.user)
        self.assertIsNotNone(self.metadata.date_created)
        self.assertIsNotNone(self.metadata.last_update)

    def test_metadata_str(self):
        """Metadata String"""
        self.assertEqual(self.metadata.__str__(), '1')