from rest_framework.serializers import (
    HyperlinkedModelSerializer, 
    SerializerMethodField
)
from django.contrib.auth.models import User


class UserSerializer(HyperlinkedModelSerializer):
    roles = SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'email',
            'roles'
        ]

    def get_roles(self, obj):
        groups = []
        for group in obj.groups.all():
            groups.append(group.name)
        return groups