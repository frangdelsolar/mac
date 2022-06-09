from django.urls import path, include
from rest_framework import routers

from .views import PersonViewSet


app_name = 'person-api'

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),

]