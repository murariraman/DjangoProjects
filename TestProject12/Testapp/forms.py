from django import forms

class Registrationform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.PasswordInput()


    
