from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from client.models import Client, ClientType, ClientPlan
from client.api.serializers import ClientTypeSerializer, ClientPlanSerializer, ClientSerializer
from users.enum import UserRoles
from users.models import Profile

from django.contrib.auth import get_user_model 

User = get_user_model()



class ClientTypeViewSet(viewsets.ModelViewSet):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer


class ClientPlanViewSet(viewsets.ModelViewSet):
    queryset = ClientPlan.objects.all()
    serializer_class = ClientPlanSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.none()
    serializer_class = ClientSerializer

    def list(self, request):
        queryset = Client.objects.none()

        profile = Profile.get_by_user(request.user)
        if not profile:
            return Response(data={'Error': 'El usuario no tiene un perfil configurado'}, status=500)

        user_roles = profile.get_user_groups_list()
        if UserRoles.APP_ADMINISTRATOR.value in user_roles:
            queryset = Client.objects.all()

        else:
            if not profile.client:
                return Response(data={'Error': 'El perfil de usuario no tiene un cliente configurado'}, status=500)
            queryset = Client.objects.filter(id=profile.client.id)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        profile = Profile.get_by_user(request.user)
        if not profile:
            return Response(data={'Error': 'El usuario no tiene un perfil configurado'}, status=500)

        user_roles = profile.get_user_groups_list()
        if not UserRoles.APP_ADMINISTRATOR.value in user_roles:
            return Response(data={'Error': 'El usuario no tiene permiso para crear un cliente'}, status=403)

        name = request.data.get('name')
        administrator_id = request.data.get('administrator_id')
        client_plan_id = request.data.get('client_plan_id')
        client_type_id = request.data.get('client_type_id')

        if not (name and client_plan_id and client_type_id):
            return Response(data={'Error': 'Faltan datos para proceder con el registro'}, status=500)

        serializer = ClientSerializer(data = {'name': name})
        serializer_is_valid = serializer.is_valid()
        
        if not serializer_is_valid:
            return Response(data={'Error': 'Los datos no son válidos'}, status=500)

        instance = serializer.save()
        instance.client_plan = ClientPlan.objects.get(id=client_plan_id)
        instance.client_type = ClientType.objects.get(id=client_type_id)

        if administrator_id:
            instance.administrator = User.objects.get(id=administrator_id)

        instance.save()
        return Response(ClientSerializer(instance).data)

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass