from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    SerializerMethodField
)
from professional.models import Professional
from person.api.serializers import PersonSerializer

class ProfessionalSerializer(HyperlinkedModelSerializer):
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    profile_id = SerializerMethodField()
    contact_id = SerializerMethodField()
    client_id = SerializerMethodField()
    class Meta:
        model = Professional
        fields = ['id', 'first_name', 'last_name', 'profile_id', 'contact_id', 'client_id']

    def get_first_name(self, obj):
        return obj.contact.first_name

    def get_last_name(self, obj):
        return obj.contact.last_name

    def get_profile_id(self, obj):
        return obj.profile.user.id

    def get_contact_id(self, obj):
        return obj.contact.id

    def get_client_id(self, obj):
        try:
            return obj.profile.client.id
        except:
            return -1