from re import L
from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
#from TestProject1.Testapp.forms import Signupform
from Testapp.forms import Signupformapna
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
# defining the signup form 

def signup(request):
    if request.method=='POST':
        fm=Signupformapna(request.POST)
        if fm.is_valid():
            messages.success(request, 'account has been created successfully')
            fm.save()
            

    else:
        fm=Signupformapna()

    return render (request, 'Testapp/signup.html', {'fmkey':fm})

def loginpage(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user1=authenticate(username=uname, password=upass)
                if user1 is not None:
                    login(request,user1)
                    return HttpResponseRedirect('/profile/')

        else:
            fm=AuthenticationForm()
    
    return render(request, 'Testapp/login.html', {'form':fm})

def logoutpage(request):
    logout(request)
    return HttpResponseRedirect('/loginpage/')

def profile(request):

    if request.user.is_authenticated:
        return render(request, 'Testapp/profile.html')

    else:
        return render(request, 'Testapp/profile.html')




# Create your views here.