from users.models import Profile
from person.models import Person
from client.models import Client
# from professional.models import Professional
# from patient.models import Patient
from rest_framework import viewsets, filters
from rest_framework.response import Response

from django.contrib.auth.models import User, Group
from .serializers import ProfileSerializer, UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from decorators.user_has_client import user_has_client
from utils.filter_queryset import filter_queryset
from users.enum import UserRoles
from utils.authentication.get_profile_and_roles import get_profile_and_roles
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import Group


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    search_fields = ['id', 'person__first_name', 'person__last_name']
    ordering_fields = ['id', 'person__first_name', 'person__last_name']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.none()
    serializer_class = UserSerializer
    search_fields = ['id', 'username', 'first_name', 'last_name', 'email']
    ordering_fields = ['id', 'username', 'first_name', 'last_name', 'email']

    
    @user_has_client
    def list(self, request):
        profile, user_roles = get_profile_and_roles(request)

        if UserRoles.APP_ADMINISTRATOR.value in user_roles:
            self.queryset = User.objects.all()
        else:
            self.queryset = User.objects.filter(id=request.user.id)

        filtered_qs = filter_queryset(self.search_fields, self.queryset, request)
        ordered_qs = filtered_qs.order_by(*request.GET.getlist('ordering'))
        serializer = self.serializer_class(ordered_qs, many=True)
        paginator = PageNumberPagination()

        page = paginator.paginate_queryset(serializer.data, request)
        if page is not None:
            return paginator.get_paginated_response(page)
        return Response(serializer.data)

    @user_has_client
    def create(self, request): 
        profile, user_roles = get_profile_and_roles(request)

        if not UserRoles.APP_ADMINISTRATOR.value in user_roles:
            return Response(data={'error': 'El usuario no tiene permiso de realizar esta acción'}, status=403)

        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        roles = request.data.get('roles')
        if not username:
            return Response(data={'error': 'Faltan datos para proceder con el registro'}, status=500)

        serializer = UserSerializer(data = {
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
            })
        serializer_is_valid = serializer.is_valid()
        if not serializer_is_valid:
            return Response(data={'error': 'Los datos no son válidos'}, status=500)

        instance = serializer.save()
        for role in roles:
            group = Group.objects.get(name=role)
            instance.groups.add(group)
        instance.save()
        return Response(UserSerializer(instance).data)

    @user_has_client
    def retrieve(self, request, pk=None):    
        profile, user_roles = get_profile_and_roles(request)

        if not (UserRoles.APP_ADMINISTRATOR.value in user_roles or
            request.user.id == pk):
            return Response(data={'error': 'El usuario no tiene permiso de realizar esta acción'}, status=403)

        filtered_objects = User.objects.filter(id=pk)
        if filtered_objects.count() <= 0:
            return Response(data={'error': 'Objeto inexistente'}, status=500)

        instance = filtered_objects.last()
        serializer = self.serializer_class(instance)

        return Response(serializer.data)


    @user_has_client
    def update(self, request, pk=None):
        profile, user_roles = get_profile_and_roles(request)

        if not (UserRoles.APP_ADMINISTRATOR.value in user_roles or
                request.user.id == pk):
            return Response(data={'error': 'El usuario no tiene permiso para actualizar este objeto'}, status=403)

        filtered_objects = User.objects.filter(id=pk)
        if filtered_objects.count() <= 0:
            return Response(data={'error': 'Objeto inexistente'}, status=500)

        instance = filtered_objects.last()

        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        roles = request.data.get('roles')

        if username: instance.username = username 
        if first_name: instance.first_name = first_name 
        if last_name: instance.last_name = last_name 
        if email: instance.email = email 

        if roles:
            for role in roles:
                group = Group.objects.get(name=role)
                instance.groups.add(group)

        instance.save()

        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    @user_has_client
    def destroy(self, request, pk=None):
        profile, user_roles = get_profile_and_roles(request)

        if not UserRoles.APP_ADMINISTRATOR.value in user_roles:
            return Response(data={'error': 'El usuario no tiene permiso para eliminar este objeto'}, status=403)

        filtered_clients = User.objects.filter(id=pk)
        if filtered_clients.count() <= 0:
            return Response(data={'error': 'Objeto inexistente'}, status=500)

        instance = filtered_clients.last()
        instance.delete()

        return Response(data={'Success': 'Objeto eliminado de manera exitosa'}, status=200)
        

