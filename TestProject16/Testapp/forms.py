from dataclasses import fields
from django import forms
from Testapp.models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name', 'email', 'password']


