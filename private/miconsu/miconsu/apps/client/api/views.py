from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from client.models import Client, ClientType, ClientPlan
from client.api.serializers import ClientTypeSerializer, ClientPlanSerializer, ClientSerializer
from utils.authentication.get_profile_and_roles import get_profile_and_roles
from utils.filter_queryset import filter_queryset
from django.contrib.auth import get_user_model 
from users.enum import UserRoles
from decorators.user_has_client import user_has_client
from rest_framework.pagination import PageNumberPagination

User = get_user_model()


class ClientTypeViewSet(viewsets.ModelViewSet):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer


class ClientPlanViewSet(viewsets.ModelViewSet):
    queryset = ClientPlan.objects.none()
    serializer_class = ClientPlanSerializer
    search_fields = ['id', 'name']
    ordering_fields = ['id', 'name']

    @user_has_client
    def list(self, request):
        self.queryset = ClientPlan.objects.all()
        filtered_qs = filter_queryset(self.search_fields, self.queryset, request)
        ord_qs = filtered_qs.order_by(*request.GET.getlist('ordering'))
        serializer = self.serializer_class(ord_qs, many=True)
        paginator = PageNumberPagination()

        page = paginator.paginate_queryset(serializer.data, request)
        if page is not None:
            return paginator.get_paginated_response(page)
        return Response(serializer.data)

    @user_has_client
    def create(self, request): 
        profile, user_roles = get_profile_and_roles(request)

        if not UserRoles.APP_ADMINISTRATOR.value in user_roles:
            return Response(data={'Error': 'El usuario no tiene permiso de realizar esta acción'}, status=403)

        name = request.data.get('name')
        if not name:
            return Response(data={'Error': 'Faltan datos para proceder con el registro'}, status=500)

        serializer = ClientPlanSerializer(data = {'name': name})
        serializer_is_valid = serializer.is_valid()
        if not serializer_is_valid:
            return Response(data={'Error': 'Los datos no son válidos'}, status=500)

        instance = serializer.save()
        return Response(ClientPlanSerializer(instance).data)

    @user_has_client
    def retrieve(self, request, pk=None):    
        profile, user_roles = get_profile_and_roles(request)

        filtered_clients = ClientPlan.objects.filter(id=pk)
        if filtered_clients.count() <= 0:
            return Response(data={'Error': 'Plan de servicios inexistente'}, status=500)

        instance = filtered_clients.last()
        serializer = self.serializer_class(instance)

        return Response(serializer.data)


    @user_has_client
    def update(self, request, pk=None):
        profile, user_roles = get_profile_and_roles(request)

        if not UserRoles.APP_ADMINISTRATOR.value in user_roles:
            return Response(data={'Error': 'El usuario no tiene permiso para actualizar este objeto'}, status=403)

        filtered_clients = ClientPlan.objects.filter(id=pk)
        if filtered_clients.count() <= 0:
            return Response(data={'Error': 'Objeto inexistente'}, status=500)

        instance = filtered_clients.last()

        name = request.data.get('name')
        if name:
            instance.name = name
        instance.save()

        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    @user_has_client
    def destroy(self, request, pk=None):
        profile, user_roles = get_profile_and_roles(request)

        if not UserRoles.APP_ADMINISTRATOR.value in user_roles:
            return Response(data={'Error': 'El usuario no tiene permiso para eliminar este objeto'}, status=403)

        filtered_clients = ClientPlan.objects.filter(id=pk)
        if filtered_clients.count() <= 0:
            return Response(data={'Error': 'Objeto inexistente'}, status=500)

        instance = filtered_clients.last()
        instance.delete()


        return Response(data={'Success': 'Objeto eliminado de manera exitosa'}, status=200)
        


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.none()
    serializer_class = ClientSerializer

    @user_has_client
    def list(self, request):
        profile, user_roles = get_profile_and_roles(request)

        if UserRoles.APP_ADMINISTRATOR.value in user_roles:
            self.queryset = Client.objects.all()
        else:
            self.queryset = Client.objects.filter(id=profile.client.id)

        serializer = self.serializer_class(self.queryset, many=True)

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(serializer.data, request)
        if page is not None:
            return paginator.get_paginated_response(page)

        return Response(serializer.data)

    @user_has_client
    def create(self, request): 
        profile, user_roles = get_profile_and_roles(request)

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

    @user_has_client
    def retrieve(self, request, pk=None):    
        profile, user_roles = get_profile_and_roles(request)

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

    @user_has_client
    def update(self, request, pk=None):
        profile, user_roles = get_profile_and_roles(request)


        if not UserRoles.APP_ADMINISTRATOR.value in user_roles:
            return Response(data={'Error': 'El usuario no tiene permiso para actualizar este cliente'}, status=403)

        filtered_clients = Client.objects.filter(id=pk)
        if filtered_clients.count() <= 0:
            return Response(data={'Error': 'Cliente inexistente'}, status=500)

        instance = filtered_clients.last()

        name = request.data.get('name')
        administrator_id = request.data.get('administrator_id')
        client_plan_id = request.data.get('client_plan_id')
        client_type_id = request.data.get('client_type_id')

        if name:
            instance.name = name
        
        if administrator_id:
            filtered_users = User.objects.filter(id=administrator_id)
            if filtered_users.count() <= 0:
                return Response(data={'Error': 'Administrador inexistente'}, status=500)
            instance.administrator = filtered_users.last()
        

        if client_plan_id:
            filtered_cps = ClientPlan.objects.filter(id=client_plan_id)
            if filtered_cps.count() <= 0:
                return Response(data={'Error': 'Plan inexistente'}, status=500)
            instance.client_plan = filtered_cps.last()

        if client_type_id:
            filtered_cts = ClientType.objects.filter(id=client_type_id)
            if filtered_cts.count() <= 0:
                return Response(data={'Error': 'Tipo de cliente inexistente'}, status=500)
            instance.client_type = filtered_cts.last()

        instance.save()

        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    @user_has_client
    def destroy(self, request, pk=None):
        profile, user_roles = get_profile_and_roles(request)

        if not UserRoles.APP_ADMINISTRATOR.value in user_roles:
            return Response(data={'Error': 'El usuario no tiene permiso para eliminar este cliente'}, status=403)

        filtered_clients = Client.objects.filter(id=pk)
        if filtered_clients.count() <= 0:
            return Response(data={'Error': 'Cliente inexistente'}, status=500)

        instance = filtered_clients.last()
        instance.delete()

        return Response(data={'Success': 'Cliente eliminado de manera exitosa'}, status=200)
        