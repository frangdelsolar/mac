from django.contrib import admin
from .models import Client, ClientPlan, ClientType


admin.site.register(Client)
admin.site.register(ClientPlan)
admin.site.register(ClientType)
