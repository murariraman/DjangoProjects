from django import forms

class testadmissionform(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()

    
