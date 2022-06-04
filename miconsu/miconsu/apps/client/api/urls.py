from django.urls import path, include
from rest_framework import routers

from .views import ClientViewSet, ClientTypeViewSet, ClientPlanViewSet


app_name = 'client-api'

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'client-type', ClientTypeViewSet)
router.register(r'client-plan', ClientPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]