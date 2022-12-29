from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MuseumUser


class MuseumUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Пошта')
    username = forms.CharField(max_length=150, required=True, label="Ім'я та прізвище")
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Ваш пароль. Повинен бути більше 8 символів.",
    )
    password2 = forms.CharField(
        label="Підтвердження пароля",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text="Введіть пароль ще раз, для підтвердження.",
    )

    class Meta(UserCreationForm):
        model = MuseumUser
        fields = ('username', 'email')


class MuseumUserChangeForm(UserChangeForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=150, required=True, label="Ім'я та прізвище")

    class Meta(UserCreationForm):
        model = MuseumUser
        fields = ('username', 'email')
