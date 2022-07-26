from django.urls import path
from .import views

urlpatterns = [
    path('',views.list_fund,name='fund_form'),
    path('fund/',views.verification_table,name='fund_table'),
    path('enregistrement_fund/',views.enregistrement_fund,name='enregistrement_fund'),
    path('enregistrement_gp/',views.enregistrement_gp,name='enregistrement_gp'),
    path('enregistrement_geo/',views.enregistrement_geo,name='enregistrement_geo'),
    path('enregistrement_assettype/', views.enregistrement_assettype, name='enregistrement_assettype'),
    path('enregistrement_trimestre/', views.enregistrement_trimestre, name='enregistrement_trimestre'),
]