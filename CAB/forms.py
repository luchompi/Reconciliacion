from django import forms
from .models import ImportarCAB,Cab

class ExcelModelForm(forms.ModelForm):
    class Meta:
        model = ImportarCAB
        fields = ('nombre_archivo','file_name',)

class PafModelForm(forms.ModelForm):
    class Meta:
        model = Cab
        fields = ('departamento_municipio','person_id','ciclo','convenio','tipo_doc','documento','apellidos','nombre','segundo_nombre','tipo_bono','formulario','fecha_expedicion','fecha_vencimiento','fecha_caducidad','valor','scope_account','scope_payment_st','scope_payment_dt',)
    
 
    