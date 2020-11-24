from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager

# Create your models here.
class Role(models.Model):
    '''
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    '''
    class RoleChoices(models.IntegerChoices):
        SUPERUSER = 0
        SUPERVISOR = 1
        ABM = 2

    id = models.PositiveSmallIntegerField(_("Name"), choices=RoleChoices.choices, primary_key=True)

    def __str__(self):
      return self.get_id_display()

class User(AbstractUser):
    class Meta:
        ordering = ["email"]

    username = None
    role = models.ManyToManyField('Role')
    email = models.EmailField(_("email address"), unique=True)
    birth_date = models.DateField(_("birth date"), null=True, blank=True)
    phone = PhoneNumberField(_("phone humber"), null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
