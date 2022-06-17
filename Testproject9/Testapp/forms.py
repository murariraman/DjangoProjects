import django


from django import forms

class StudentRegister(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()

    
