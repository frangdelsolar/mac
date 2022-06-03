from django.test import TestCase
from .models import Metadata
from django.contrib.auth import get_user_model


User = get_user_model()

class MetadataTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="pepe", password="1234")
        metadata = Metadata.objects.create(created_by=user, updated_by=user)

    def test_metadata_init(self):
        """Metadata adds timestamp and user"""
        md = Metadata.objects.get(created_by=self.user)
        print(md)
        # self.assertEqual(lion.speak(), 'The lion says "roar"')
        # self.assertEqual(cat.speak(), 'The cat says "meow"')