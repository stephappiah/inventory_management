from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=60, unique=True, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    first_name = models.CharField(blank=True, max_length=100)
    last_name= models.CharField(blank=True, max_length=100)
    

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.first_name != None and self.last_name != None:
            return self.first_name + ' ' + self.last_name
        elif self.first_name == None:
            return self.last_name
        else:
            return self.first_name 

    def get_call_contact(self):
        return self.contact

    def get_short_name(self):
        if self.first_name == None:
            return self.last_name
        else:
            return self.first_name