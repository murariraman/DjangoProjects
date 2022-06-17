from django.shortcuts import render
from Testapp.models import User
from Testapp.forms import StudentRegistration
from django.http import HttpResponseRedirect

# Create your views here.

def createfunction(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=User(name=nm, email=em, password=pwd)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
          
    return render(request, 'Testapp/create.html', {'formkey': fm})


def readordisplayfunction(request):
    
    stdone=User.objects.all()
    return render(request, 'Testapp/readordisplay.html', {'stdkey':stdone})

def deletefunction(request, id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()

    
    return render(request, 'Testapp/delete.html', {'id':id})



def updatefunction(request,id):
    pi=User.objects.get(pk=id)
    fm=StudentRegistration(instance=pi)

    if request.method=='POST':
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            fm=StudentRegistration()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)

    
    return render(request, 'Testapp/update.html', {'form1':fm},)