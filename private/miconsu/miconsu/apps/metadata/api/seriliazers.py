from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    DateField,
    SerializerMethodField
)
from metadata.models import Metadata


class MetadataSerializer(HyperlinkedModelSerializer):
    client_id = SerializerMethodField()
    created_by = SerializerMethodField()
    updated_by = SerializerMethodField()

    class Meta:
        model = Metadata
        fields = [
            'client_id',
            'created_by',
            'updated_by',
            'date_created',
            'last_update',
        ]


    def get_client_id(self, obj):
        if obj.client:
            return obj.client.id
        return None

    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.username
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.username
        return None