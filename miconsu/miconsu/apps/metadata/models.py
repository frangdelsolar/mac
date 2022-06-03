from django.db import models
from django.contrib.auth import get_user_model


class Metadata(models.Model):
    # client = models.ForeignKey('client.Client', on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="created_by", null=True, blank=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="updated_by", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)