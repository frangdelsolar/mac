from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    person = models.ForeignKey('person.Person', on_delete=models.CASCADE, verbose_name='Persona', null=True, blank=True)
    client = models.ForeignKey('client.Client', on_delete=models.PROTECT, verbose_name='Cliente', blank=True, null=True)

    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuario'

    def __str__(self):
        return f'{self.user.username}'

    @classmethod
    def get_by_user_id(self, id):
        return Profile.objects.get(user__id = id)

    @classmethod
    def get_by_user(self, user):
        qs = Profile.objects.filter(user=user)
        if qs.count() <= 0:
            return None
        return qs.last()

    def get_user_groups_list(self): 
        return list(self.user.groups.values_list('name', flat=True))