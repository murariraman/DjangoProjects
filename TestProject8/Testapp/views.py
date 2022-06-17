from django.shortcuts import render
from pkg_resources import safe_extra

from Testapp.forms import StudentAdmission

def studentadmissionview(request):

    sa=StudentAdmission()
    return render(request, 'Testapp/admission.html',{'formstudent':sa})

# Create your views here.
