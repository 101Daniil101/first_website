from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from . import forms

def login_user(request):
    if request.method == 'POST':
        form = forms.LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect('')
    else:
        form = forms.LoginUserForm()
    return render(request, 'users/login.html', {'form': form})

def register_user(request):
    return render(request, 'users/register.html')
