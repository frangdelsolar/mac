from django.db import models
from django.contrib.auth import get_user_model


class ClientType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Tipo de cliente'
        verbose_name_plural = 'Tipos de cliente'

    def __str__(self):
        return self.name


class ClientPlan(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Plan de cliente'
        verbose_name_plural = 'Planes de cliente'

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=255)
    administrator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Administrador', related_name='client_administered', null=True, blank=True)
    client_plan = models.ForeignKey('client.ClientPlan', on_delete=models.CASCADE, verbose_name='Plan', related_name="client_plan")
    client_type = models.ForeignKey('client.ClientType', on_delete=models.CASCADE, verbose_name='Tipo de cliente', related_name="client_plan")

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name
