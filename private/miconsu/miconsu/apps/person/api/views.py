from rest_framework import viewsets
from person.models import Person
from .serializers import PersonSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    # permission_classes = [IsAuthenticated]
