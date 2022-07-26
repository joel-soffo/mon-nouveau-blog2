from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import Personnel
def list_personnel(request):
    if request.method == 'POST':
        form3 = PersonnelForm(request.POST)

        if form3.is_valid():
            form3.save()

        return HttpResponseRedirect('/personnel/')
    else:
        form3 = PersonnelForm()
    return render(request, 'personnel/personnal_update.html',{'form3':form3})

def enregistrement_personnel(request):
    if request.method =='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        email = request.POST['email']
        perso1 = Personnel.objects.create(prenoms_perso=firstname,name_per=lastname,email_perso=email,password=password)
        perso1.save()




        # perso = Personnel.objects.create(prenoms_perso = nom.objects.get(pren= firstname)) pour les champs avec les cles étrangères

        return render(request,'personnel/personnal_update.html')

    return render(request,'personnel/personnal_update.html')




