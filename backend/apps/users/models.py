from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

from .managers import UserManager

##THIRDPARTY
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):

    """User model."""

    username = models.CharField(max_length=50, null=True)
    first_name = None
    last_name = None
    email = models.EmailField(('Email institucional'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #asked in console

    objects = UserManager()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class Role(models.Model):
    
    name = models.CharField('Nombre', max_length=30)

    def __str__(self):
        texto = '{}'.format(
            self.name,
        )
        return texto

class Person(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doc_number = models.CharField('DNI', max_length=13, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Rol')
    first_name = models.CharField('Primer nombre', max_length=15)
    middle_name = models.CharField('Segundo nombre', max_length=15, blank=True, null=True)
    first_lastname = models.CharField('Primer apellido', max_length=15)
    second_lastname = models.CharField('Segundo apellido', max_length=15, blank=True, null=True)
    personal_email = models.EmailField('Email personal', max_length=40, blank=True, null=True)
    birthday = models.DateField('Fecha de nacimiento', blank=True, null=True)
    birth_place = models.CharField('Lugar de nacimiento', max_length=15, blank=True, null=True)
    nationality = CountryField('Nacionalidad', blank_label='Selecciona un país', null=True)
    CHOICES_GENDER = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Sin genero', 'Sin genero'),
        ('Sin especificar', 'Sin especificar'),
    ]
    gender = models.CharField(
        'Género',
        max_length=20,
        choices = CHOICES_GENDER,
        default='Sin especificar',
        )
    address = models.CharField('Dirección', max_length=15, blank=True, null=True)
    neighborhood = models.CharField('Barrio', max_length=15, blank=True, null=True)
    phone = models.CharField('Nro de teléfono', max_length=15, blank=True, null=True)
    STATE_CHOICES = [
        ('Soltero', 'Soltero'),
        ('Casado', 'Casado'),
        ('Divorciado', 'Divorciado'),
        ('Viudo/a', 'Viudo/a'),
        ('No aplica', 'No aplica'),
    ]
    marital_status = models.CharField(
        'Estado civil',
        max_length=20,
        choices = STATE_CHOICES,
        default='No aplica',
        null=True,
        )
    created_date = models.DateField('Fecha de alta')

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['first_name']
    
    def __str__(self):
        texto = '{} {}'.format(
            self.first_name,
            self.first_lastname,
        )
        return texto

