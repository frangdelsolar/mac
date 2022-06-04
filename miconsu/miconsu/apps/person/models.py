from django.db import models
from django.utils.text import slugify
from metadata.models import Metadata
import datetime
import itertools
from person.enum.gender import GenderEnum
from person.enum.level_of_studies import LevelOfStudiesEnum
from person.enum.marital_status import MaritalStatusEnum


class Person(models.Model):
    metadata = models.OneToOneField('metadata.Metadata', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    dni = models.CharField(max_length=25, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True, choices=[(tag.name, tag.value) for tag in GenderEnum])
    date_of_birth = models.DateField(auto_now=False, null=True, blank=True)
    marital_status = models.CharField(max_length=30, null=True, blank=True, choices=[(tag.name, tag.value) for tag in MaritalStatusEnum])
    level_of_studies = models.CharField(max_length=30, null=True, blank=True, choices=[(tag.name, tag.value) for tag in LevelOfStudiesEnum])
    occupation = models.CharField(max_length=120, null=True, blank=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        today = datetime.date.today()
        if self.date_of_birth:
            return int((today - self.date_of_birth).days // 365.25)
        return 0