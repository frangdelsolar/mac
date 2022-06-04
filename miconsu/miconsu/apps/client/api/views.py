from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from client.models import Client, ClientType, ClientPlan
from client.api.serializers import ClientTypeSerializer, ClientPlanSerializer, ClientSerializer
from users.enum import UserRoles
from users.models import Profile


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

