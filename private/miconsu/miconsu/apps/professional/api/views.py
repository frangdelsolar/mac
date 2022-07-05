from rest_framework import viewsets
from professional.models import Professional
from .serializers import ProfessionalSerializer
from decorators.user_has_client import user_has_client
from utils.filter_queryset import filter_queryset
from users.enum import UserRoles
from utils.authentication.get_profile_and_roles import get_profile_and_roles
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import Group
from rest_framework.response import Response
from metadata.models import Metadata
from users.models import Profile
from person.models import Person

class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = Professional.objects.none()
    serializer_class = ProfessionalSerializer
    search_fields = ['id', 'profile__user__username', 'contact__first_name', 'contact__last_name']
    ordering_fields = ['id', 'profile__user__username', 'contact__first_name', 'contact__last_name']

    
    @user_has_client
    def list(self, request):
        profile, user_roles = get_profile_and_roles(request)

        if UserRoles.APP_ADMINISTRATOR.value in user_roles:
            self.queryset = Professional.objects.all()
        elif UserRoles.ORGANIZATION_ADMINISTRATOR.value in user_roles:
            self.queryset = Professional.objects.filter(metadata__client=profile.client)
        elif UserRoles.PROFESSIONAL.value in user_roles:
            self.queryset = Professional.objects.filter(metadata__client=profile.client)

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

        if not (UserRoles.APP_ADMINISTRATOR.value in user_roles or UserRoles.ORGANIZATION_ADMINISTRATOR.value in user_roles):
            return Response(data={'error': 'El usuario no tiene permiso de realizar esta acción'}, status=403)

        prof_profile = request.data.get('profile_id')
        prof_contact = request.data.get('contact_id')
        if not (prof_profile and prof_contact):
            return Response(data={'error': 'Faltan datos para proceder con el registro'}, status=500)

        prof_client = request.data.get('client_id')
        if not (prof_client):
            prof_client = profile.client.id

        metadata = Metadata.objects.create(
            client_id = prof_client,
            created_by= request.user,
        )

        prof_profile_filter = Profile.objects.filter(user=prof_profile)
        prof_contact_filter = Person.objects.filter(id=prof_contact)
        if prof_profile_filter.count() <= 0 or prof_contact_filter.count() <= 0:
             return Response(data={'error': 'Datos erróneos'}, status=500)

        instance = Professional.objects.create(
            profile = prof_profile_filter.last(),
            contact = prof_contact_filter.last()
        )

        return Response(ProfessionalSerializer(instance).data)

    @user_has_client
    def retrieve(self, request, pk=None):    
        profile, user_roles = get_profile_and_roles(request)

        filtered_objects = Professional.objects.filter(id=pk)
        if filtered_objects.count() <= 0:
            return Response(data={'error': 'Objeto inexistente'}, status=500)

        instance = filtered_objects.last()
        if not (UserRoles.APP_ADMINISTRATOR.value in user_roles or
                profile.client == instance.metadata.client):
            return Response(data={'error': 'El usuario no tiene permiso de realizar esta acción'}, status=403)

        serializer = self.serializer_class(instance)

        return Response(serializer.data)


    @user_has_client
    def update(self, request, pk=None):
        profile, user_roles = get_profile_and_roles(request)

        filtered_objects = Professional.objects.filter(id=pk)
        if filtered_objects.count() <= 0:
            return Response(data={'error': 'Objeto inexistente'}, status=500)

        instance = filtered_objects.last()
        if not (UserRoles.APP_ADMINISTRATOR.value in user_roles or
                profile.client == instance.metadata.client):
            return Response(data={'error': 'El usuario no tiene permiso de realizar esta acción'}, status=403)

        prof_profile = request.data.get('profile')
        prof_contact = request.data.get('contact')

        if prof_profile: instance.profile = prof_profile 
        if prof_contact: instance.contact = prof_contact 
        instance.save()

        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    @user_has_client
    def destroy(self, request, pk=None):
        profile, user_roles = get_profile_and_roles(request)

        filtered_objects = Professional.objects.filter(id=pk)
        if filtered_objects.count() <= 0:
            return Response(data={'error': 'Objeto inexistente'}, status=500)

        instance = filtered_objects.last()
        if not (UserRoles.APP_ADMINISTRATOR.value in user_roles or
                profile.client == instance.metadata.client):
            return Response(data={'error': 'El usuario no tiene permiso de realizar esta acción'}, status=403)

        instance.delete()

        return Response(data={'Success': 'Objeto eliminado de manera exitosa'}, status=200)
        


