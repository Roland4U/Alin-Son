from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, User


class UserRegForm(UserCreationForm):
    email = forms.EmailField()

    email.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 

