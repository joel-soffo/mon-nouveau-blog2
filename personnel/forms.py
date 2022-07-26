from django import forms
from .models import *


class PersonnelForm(forms.ModelForm):
    class Meta :
        model =Personnel
        fields = '__all__'
