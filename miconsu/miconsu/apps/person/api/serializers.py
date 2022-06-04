from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    SerializerMethodField,
    DateField
)
from person.models import Person
from metadata.api.seriliazers import MetadataSerializer


class PersonSerializer(HyperlinkedModelSerializer):
    metadata = MetadataSerializer()
    full_name = SerializerMethodField()
    gender = SerializerMethodField()
    date_of_birth = DateField()
    marital_status = SerializerMethodField()
    level_of_studies = SerializerMethodField()
    
    class Meta:
        model = Person
        fields = [
            'id',
            'metadata',
            'first_name',
            'last_name',
            'full_name',
            'dni',
            'gender',
            'date_of_birth',
            'marital_status',
            'level_of_studies',
            'occupation',
        ]

    def get_full_name(self, obj):
        return obj.get_full_name()

    def get_gender(self, obj):
        return obj.get_gender_display()

    def get_marital_status(self, obj):
        return obj.get_marital_status_display()

    def get_level_of_studies(self, obj):
        return obj.get_level_of_studies_display()
