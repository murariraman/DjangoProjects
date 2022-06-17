from django.shortcuts import render

# Create your views here.

def homeone(request):
    return render(request, 'Testapp/home.html')


def showone(request, my_id):
    print(my_id)
    if my_id=='1':
        student={'idone':my_id, 'name':'raman'}

    if my_id=='2':
        student={'idone':my_id, 'name':'raman'}

    if my_id=='3':
        student={'idone':my_id, 'name':'raman'}

    if my_id=='4':
        student={'idone':my_id, 'name':'raman'}
    return render(request, 'Testapp/show.html', {'stdone':student})


def showonesubdetails(request, my_id, my_subid):
    if my_id=='1' and my_subid=='5':
        student1={'id': my_id,'subid':my_subid, 'details':'my subdetais'}

    if my_id=='2' and my_subid=='6':
        student1={'id':my_id,'subid':my_subid, 'details':'my subdetais'}

    if my_id=='3' and my_subid=='7':
        student1={'id':my_id,'subid':my_subid, 'details':'my subdetais'}

    return render(request, 'Testapp/showonesubdetails.html', {'std1':student1})




