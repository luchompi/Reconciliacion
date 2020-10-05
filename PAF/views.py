from django.shortcuts import render,redirect
from .forms import ExcelModelForm,PafModelForm
from PAF.models import *
from django.urls import reverse_lazy
import pymysql
import django_excel as excel
import pymysql.cursors
import pandas as pd
import numpy as np


from django.views.generic import ListView,UpdateView, DeleteView,CreateView

#Carga de los XLSX
def upload(request):
	form = ExcelModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		form = ExcelModelForm
		file_name = request.FILES['file_name']
		pymysql.converters.encoders[np.int64] = pymysql.converters.escape_int
		pymysql.converters.conversions = pymysql.converters.encoders.copy()
		pymysql.converters.conversions.update(pymysql.converters.decoders)
		connection=pymysql.connect(host='localhost',
			user='root',
			password='',
			db='db_practica',
			charset='utf8mb4',
			cursorclass=pymysql.cursors.DictCursor)
		try:
			with connection.cursor() as cursor:
				df = pd.read_excel(file_name,skiprows = 2,
		                 names=['DEPARTAMENTO','MUNICIPIO','SERIAL','NUMERO DEL CONVENIO','CONVENIO','TIPO_DOC','DOCUMENTO',
		                 'NOMBRE','TIPO_BONO','FORMULARIO','FECHA_EXPEDICION','FECHA_VENCIMIENTO','FECHA_CADUCIDAD','VALOR'],sheet_name='Report')
				df.keys()
				for i in range(0,len(df)):
					sql="INSERT INTO paf_paf(departamento,municipio,serial,numeroConvenio,convenio,tipo_doc,documento,nombre,tipo_bono,formulario,fecha_expedicion,fecha_vencimiento,fecha_caducidad,valor) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
					cursor.execute(sql,[df['DEPARTAMENTO'][i],df['MUNICIPIO'][i],df['SERIAL'][i],df['NUMERO DEL CONVENIO'][i],df['CONVENIO'][i],df['TIPO_DOC'][i],df['DOCUMENTO'][i],df['NOMBRE'][i],df['TIPO_BONO'][i],df['FORMULARIO'][i],df['FECHA_EXPEDICION'][i],df['FECHA_VENCIMIENTO'][i],df['FECHA_CADUCIDAD'][i],df['VALOR'][i]])
					connection.commit()
		finally:
			connection.close()
		return redirect('paf:index-archivo')
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

