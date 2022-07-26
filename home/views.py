from django.shortcuts import render


#from chartit import Chart, DataPool
# Create your views here.
def home(request):

    return render(request, 'home/home.html')
