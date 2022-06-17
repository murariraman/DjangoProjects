from django import  forms


class StudentAdmission(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()