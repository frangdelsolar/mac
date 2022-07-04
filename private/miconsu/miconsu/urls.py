from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from users.api.views import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/', include('client.api.urls', namespace='client-api')),
    path('api/', include('users.api.urls', namespace='users-api')),
    path('api/', include('person.api.urls', namespace='person-api')),
    # path('api/', include('professional.api.urls', namespace='professional-api')),
]
