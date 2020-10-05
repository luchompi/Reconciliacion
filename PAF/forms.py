from django import forms
from .models import ImportarPAF,Paf

class ExcelModelForm(forms.ModelForm):
    class Meta:
        model = ImportarPAF
        fields = ('nombre_archivo','file_name',)

class PafModelForm(forms.ModelForm):
    class Meta:
        model = Paf
        fields = ('departamento','municipio','serial','numeroConvenio','convenio','tipo_doc','documento','nombre','tipo_bono','formulario','fecha_expedicion','fecha_vencimiento','fecha_caducidad','valor',)
   