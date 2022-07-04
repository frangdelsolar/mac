from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    SerializerMethodField
)
from professional.models import Professional
from person.api.serializers import PersonSerializer

class ProfessionalSerializer(HyperlinkedModelSerializer):
    contact = SerializerMethodField()
    class Meta:
        model = Professional
        fields = ['id', 'contact']

    def get_contact(self, obj):
        return PersonSerializer(obj.contact).data