from django.db import models
from metadata.models import Metadata


class Professional(Metadata):
    profile = models.ForeignKey('users.Profile', blank=True, null=True, on_delete=models.CASCADE, related_name='professional_profile')
    contact = models.ForeignKey('person.Person', on_delete=models.CASCADE, verbose_name='Persona')
    
    class Meta:
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

    @staticmethod
    def get_professional_by_user(user):
        return Professional.objects.filter(_profile__user=user).first()

    def __str__(self):
        return self.contact.get_full_name()
