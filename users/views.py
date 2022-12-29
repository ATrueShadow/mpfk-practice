from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import Group

from users.forms import MuseumUserCreationForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = MuseumUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='visitor')
            user.groups.add(group)
            login(request, user)
            messages.success(request, 'Успішна реєстрація.')
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('/')
        messages.error(request, 'Щось пішло не так.')
    form = MuseumUserCreationForm()
    return render(request=request, template_name='registration/register.html', context={"register_form": form})
