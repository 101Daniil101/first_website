from django import forms

class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=100, label="Логин")
    password = forms.CharField(max_length=100, label="Пароль")



