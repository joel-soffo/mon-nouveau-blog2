from django.urls import path
from .import views

urlpatterns = [
    path('',views.list_personnel,name='personnal_form'),
    path('enr_personnel/', views.enregistrement_personnel, name='enr_perso'),
]