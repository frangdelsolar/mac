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
    administrator = UserSerializer()
    client_plan = ClientPlanSerializer()
    client_type = ClientTypeSerializer()
    
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
        administrator_dict = validated_data.pop('administrator')
        client_type_dict = validated_data.pop('client_type')
        client_plan_dict = validated_data.pop('client_plan')
        client = Client(**validated_data)
        admin_ser = UserSerializer(data=administrator_dict)
        admin_ser.is_valid()
        admin = admin_ser.save()
        client.administrator = admin

        cp_ser = ClientPlanSerializer(data=client_plan_dict)
        cp_ser.is_valid()
        cp = cp_ser.save()
        client.client_plan = cp

        ct_ser = ClientTypeSerializer(data=client_type_dict)
        ct_ser.is_valid()
        ct = ct_ser.save()
        client.client_type = ct

        client.save()
        return client