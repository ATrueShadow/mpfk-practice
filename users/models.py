from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import escape


# Create your models here.


class MuseumUser(AbstractUser):
    pass
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, verbose_name=_('Пошта'))
    username = models.CharField(max_length=150, unique=True, verbose_name=_("Ім'я та призвіще"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

