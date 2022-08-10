import instance as instance
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from fund.models import *
from fund.forms import *
from django.urls import reverse


# from chartit import Chart, DataPool
# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def profil_gp(request, pk=1):
    # gp=Gp.objects.get(id_gp =pk)
    gp = get_object_or_404(Gp, pk=pk)

    return render(request, 'home/gp_list_feature.html', locals())


def modifier1_gp(request, pk):
    gp = get_object_or_404(Gp, pk=pk)

    if request.method == 'POST':
        gp.name_gp = request.POST['gpname']
        gp.prenoms_manager = request.POST['firstnamemanager']
        gp.name_manager = request.POST['lastnamemanager']
        gp.mail_manager = request.POST['emailmanager']
        gp.telephone_manager = request.POST['telephone_manager']

        gp.save()
        messages.success(request, "Gp Enregistré")

    return render(request, 'fund/gp.html', locals())


def modifier_gp(request, pk):
    gp = Gp.objects.get(id_gp=pk)
    form2 = GpForm(instance=gp)
    if request.method == 'POST':
        form2 = GpForm(request.POST, instance=gp)

        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect('/')

    return render(request, 'fund/gp.html', {'form2': form2})


def supprimer_gp(request, pk=1):
    gp = Gp.objects.get(id_gp=pk)
    if request.method == 'POST':
        gp.delete()
        return HttpResponseRedirect('/')

    context = {'item': gp}

    return render(request, 'home/supprimer_gp.html', context)
