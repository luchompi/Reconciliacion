from django import forms
from .models import ImportarPAF

class ExcelModelForm(forms.ModelForm):
    class Meta:
        model = ImportarPAF
        fields = ('file_name',)