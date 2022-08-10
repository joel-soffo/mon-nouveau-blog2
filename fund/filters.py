import django_filters
from .models import *


class FundFiltre(django_filters.FilterSet):
    class Meta:
        model= Fund
        fields = ['val_annee','id_trim' , 'name_fund','open_close','structure']

class GpFiltre(django_filters.FilterSet):
    class Meta:
        model= Gp
        fields = ['name_gp']