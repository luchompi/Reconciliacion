from django.shortcuts import render
from .models import Cab
from django.views.generic import ListView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
import pymysql
import django_excel as excel
import pymysql.cursors
import pandas as pd
import numpy as np
# Create your views here.
#Index de los XLSX cargados
class index_file(ListView):
	model = Cab
	template_name = 'CAB/index_file.html'
	success_url =reverse_lazy('cab:index-archivo')

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