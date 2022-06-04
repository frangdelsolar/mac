from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('client.api.urls', namespace='client-api')),
    path('api/', include('person.api.urls', namespace='person-api')),
]
