from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Row, Column
from django import forms
from .models import *


class FUndForm(forms.ModelForm):
    name_fund = forms.CharField(help_text="Veuillez enregistrer tout le nom en miniscule")
    model = Fund
    fields_used = ['name_fund','structure']

    def __init__(self, *args, **kwargs):

        super(FUndForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'General Information related fund',
                Row(
                    Column('name_fund', css_class="col-md-6"),
                    Column('structure', css_class="col-md-6"),
                )
            ),
            *[field.name for field in self.model._meta.get_fields() if field.name not in self.fields_used],
            Row(
               Column(
                   Submit('submit', 'Submit', css_class='button white'),
                   css_class='col-md-3'
               )
            ),

        )

    class Meta :
        model = Fund
        exclude = ['id_gp']


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
