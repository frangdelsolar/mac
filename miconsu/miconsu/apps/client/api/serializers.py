from rest_framework.serializers import (
    HyperlinkedModelSerializer,
)
from client.models import Client, ClientType, ClientPlan
from users.api.serializers import UserSerializer


class ClientTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ClientType
        fields = [
            'id',
            'name',
        ]
            

class ClientPlanSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ClientPlan
        fields = [
            'id',
            'name',
        ]


class ClientSerializer(HyperlinkedModelSerializer):
    administrator = UserSerializer(read_only=True)
    client_plan = ClientPlanSerializer(read_only=True)
    client_type = ClientTypeSerializer(read_only=True)
    
    class Meta:
        model = Client
        fields = [
            'id',
            'name',
            'administrator',
            'client_plan',
            'client_type',
        ]

    def create(self, validated_data):
        return Client(**validated_data)