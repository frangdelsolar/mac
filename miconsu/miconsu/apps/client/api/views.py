from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from client.models import Client, ClientType, ClientPlan
from client.api.serializers import ClientTypeSerializer, ClientPlanSerializer, ClientSerializer
from utils.authentication.response_auth_profile_client_valid import response_auth_profile_client_valid as is_profile_valid
from utils.authentication.get_profile_and_roles import get_profile_and_roles
from django.contrib.auth import get_user_model 
from users.enum import UserRoles

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
        error_response = is_profile_valid(request)
        if error_response:
            return error_response
        
        profile, user_roles = get_profile_and_roles(request)


        if UserRoles.APP_ADMINISTRATOR.value in user_roles:
            self.queryset = Client.objects.all()
        else:
            if not profile.client:
                return Response(data={'Error': 'El perfil de usuario no tiene un cliente configurado'}, status=500)
            self.queryset = Client.objects.filter(id=profile.client.id)

        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        profile, user_roles = is_profile_valid(request)

        if not UserRoles.APP_ADMINISTRATOR.value in user_roles:
            return Response(data={'Error': 'El usuario no tiene permiso de realizar esta acción'}, status=403)

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

    def retrieve(self, request, pk=None):
        profile, user_roles = is_profile_valid(request)

        filtered_clients = Client.objects.filter(id=pk)
        if filtered_clients.count() <= 0:
            return Response(data={'Error': 'Cliente inexistente'}, status=500)

        instance = filtered_clients.last()
        serializer = self.serializer_class(instance)

        if UserRoles.APP_ADMINISTRATOR.value in user_roles:
            return Response(serializer.data)

        if instance == profile.client:
            return Response(serializer.data)
                   
        return Response(data={'Error': 'El usuario no tiene permiso para ver este cliente'}, status=500)


    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass