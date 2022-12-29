# Register your models here.

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MuseumUserCreationForm, MuseumUserChangeForm
from .models import MuseumUser


class MuseumUserAdmin(UserAdmin):
    add_form = MuseumUserCreationForm
    form = MuseumUserChangeForm
    model = MuseumUser
    list_display = ['email', 'first_name', 'last_name']


admin.site.register(MuseumUser, MuseumUserAdmin)
