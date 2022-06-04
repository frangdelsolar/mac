from rest_framework import viewsets
from client.models import Client, ClientType, ClientPlan
from client.api.serializers import ClientTypeSerializer, ClientPlanSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class ClientTypeViewSet(viewsets.ModelViewSet):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer


class ClientPlanViewSet(viewsets.ModelViewSet):
    queryset = ClientPlan.objects.all()
    serializer_class = ClientPlanSerializer


# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
