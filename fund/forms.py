from django import forms
from .models import *


class FUndForm(forms.ModelForm):
    class Meta :
        model = Fund
        fields = '__all__'

class AssettypeForm(forms.ModelForm):
    class Meta :
        model = Assettype
        fields = '__all__'


class GeoForm(forms.ModelForm):
    class Meta :
        model = Geo
        fields= '__all__'



class GpForm(forms.ModelForm):
    class Meta:
        model=Gp
        fields= '__all__'


class TrimestreForm(forms.ModelForm):
    class Meta:
        model = Trimestre
        fields = '__all__'

class AnneeForm(forms.ModelForm):
    class Meta:
        model = Annee
        fields = '__all__'
