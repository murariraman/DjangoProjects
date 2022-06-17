from email import message
from django.shortcuts import render
from Testapp.forms import TeacherRegistration
from Testapp.forms import StudentRegistration
from django.contrib import messages



def testview(request):

    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm=StudentRegistration()
            messages.info(request, 'your data has been saved successfully')

    else:
        fm=StudentRegistration()


    return render(request, 'Testapp/test.html',{'formtest':fm})

def homeview(request):
    if request.method=='POST':
        fm=TeacherRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm=TeacherRegistration()
    else:
        fm=TeacherRegistration()       



    return render(request, 'Testapp/home.html',{'formhome':fm})

# Create your views here.
