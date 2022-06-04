from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    # person = models.ForeignKey('person.Person', on_delete=models.CASCADE, verbose_name='Persona', null=True, blank=True)
    client = models.ForeignKey('client.Client', on_delete=models.PROTECT, verbose_name='Cliente', blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuario'

    def __str__(self):
        return str(self.pk)

    @classmethod
    def getByUserId(self, id):
        return Profile.objects.get(user__id = id)

    @classmethod
    def get_profile_by_user(self, user):
        return Profile.objects.get(user = user)