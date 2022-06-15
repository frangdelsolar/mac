from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, ProfileViewSet


app_name = 'users-api'

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]