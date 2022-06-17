from django.shortcuts import render

# Create your views here.

def showhtml(request, my_id):
    print(my_id)
    if my_id=='1':
        print(my_id)
        student1={'id':my_id, 'name':'rohan'}

    if my_id=='2':
        print(my_id)
        student1={'id':my_id, 'name':'sohana'}

    if my_id=='3':
        print(my_id)
        student1={'id':my_id, 'name':'sohanb'}

    if my_id=='4':
        print(my_id)
        student1={'id':my_id, 'name':'sohanc'}    

    return render(request,'Testapp/show.html',student1)


def homehtml(request):
    return render(request, 'Testapp/home.html')
