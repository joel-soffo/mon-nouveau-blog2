from django.urls import path
from .import views

urlpatterns = [
    path('',views.list_fund,name='fund_form'),
    path('table_fund/',views.verification_table,name='fund_table'),
    path('enregistrement_fund/',views.enregistrement_fund,name='enregistrement_fund'),
    path('enregistrement_gp/',views.enregistrement_gp,name='enregistrement_gp'),
    path('supprimer_fund/<int:pk>/', views.supprimer_fund, name='supprimer_fund'),
    path('enregistrement_geo/',views.enregistrement_geo,name='enregistrement_geo'),
    path('enregistrement_assettype/', views.enregistrement_assettype, name='enregistrement_assettype'),
    path('enregistrement_trimestre/', views.enregistrement_trimestre, name='enregistrement_trimestre'),
    path('enregistrement_fund_asset/', views.enregistrement_fundassettype, name='enregistrement_fundassettype'),
    path('enregistrement_fund_geo/', views.enregistrement_fundgeo, name='enregistrement_fundgeo'),
    path('historical_data/', views.historical_fund_table, name='historical_data'),
    path('profil_fund/<int:pk>/', views.profil_fund, name='profil_fund'),
    path('create_fund/', views.FundCreateView.as_view(), name='create_fund')
]