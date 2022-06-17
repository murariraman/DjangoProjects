#from dataclasses import fields
#from pyexpat import model
#
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Signupformapna(UserCreationForm):
    password2:forms.CharField(label='confirm password(again)', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email',]

        label={'email', 'Emailone'}