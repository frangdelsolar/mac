from django.test import TestCase
from metadata.models import Metadata
from django.contrib.auth import get_user_model

User = get_user_model()

class MetadataTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="pepe", password="1234")
        Metadata.objects.create(created_by=user, updated_by=user)

    def test_metadata_init(self):
        """Metadata adds timestamp and user"""
        user = User.objects.get(username="pepe")
        md = Metadata.objects.get(created_by=user)

        self.assertEqual(md.created_by, user)
        self.assertEqual(md.updated_by, user)
        self.assertIsNotNone(md.date_created)
        self.assertIsNotNone(md.last_update)

    def test_metadata_str(self):
        """Metadata String"""
        user = User.objects.get(username="pepe")
        md = Metadata.objects.get(created_by=user)

        self.assertIn("pepe", md.__str__())