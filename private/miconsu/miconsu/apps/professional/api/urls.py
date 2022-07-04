from django.urls import path, include
from rest_framework import routers

from .views import ProfessionalViewSet
from .serializers import ProfessionalSerializer


app_name = 'professional-api'

router = routers.DefaultRouter()
router.register(r'professional', ProfessionalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]