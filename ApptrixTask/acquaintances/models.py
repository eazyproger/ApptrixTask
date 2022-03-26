from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .manager import CustomUserManager


class CustomUser(AbstractBaseUser):
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='acquaintances/avatars')
    gender = models.CharField(max_length=7)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class MatchModel(models.Model):
    first_email = models.EmailField('first email address')
    second_email = models.EmailField('second email address')

    def __str__(self):
        return self.first_email + ' ' + self.second_email
