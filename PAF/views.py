from django.shortcuts import render
from .forms import ExcelModelForm,PafModelForm
from PAF.models import *
from django.urls import reverse_lazy
import pymysql
import django_excel as excel


from django.views.generic import ListView,UpdateView, DeleteView,CreateView
# Create your views here.
#Carga de los XLSX
def upload(request):
	form = ExcelModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		form = ExcelModelForm


	return render(request,'PAF/upload.html', {'form':form})

#Index de Tabla PAF 
class index(ListView):
	model = Paf
	template_name = 'PAF/index.html'

class rowPafCreate(CreateView):
    model = Paf
    form_class = PafModelForm
    template_name = "PAF/nuevo.html"

class rowPafEdit(UpdateView):
	model = Paf
	form_class = PafModelForm
	template_name= 'PAF/upload.html'
	success_url =reverse_lazy('paf:index')

class rowPafDelete(DeleteView):
    model = Paf
    template_name = "PAF/delete.html"
    success_url =reverse_lazy('paf:index')



#Index de los XLSX cargados
class index_file(ListView):
	model = ImportarPAF
	template_name = 'PAF/index_file.html'
	success_url =reverse_lazy('paf:index')


#Actualizar archivo excel cargado
class update_file(UpdateView):
	model = ImportarPAF
	form_class=ExcelModelForm
	template_name= 'PAF/upload.html'
	success_url =reverse_lazy('paf:index-archivo')

#Eliminar ARchivo excel, presenta problemas
def file_delete(request,id):
    file = ImportarPAF.objects.get(id=id)
    if request.method == 'POST':
        file.delete()
        return redirect('paf:index-archivo')
    return render(request, 'PAF/delete_file.html',{'file':file})

