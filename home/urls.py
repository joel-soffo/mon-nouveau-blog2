
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='acceuil'),

    path('profil_gp/<int:pk>/', views.profil_gp, name='profil_gp'),
    path('modifier_gp/<int:pk>/',views.modifier1_gp,name='modifier_gp'),
    path('supprimer_gp/<int:pk>/', views.supprimer_gp, name='supprimer_gp'),

]