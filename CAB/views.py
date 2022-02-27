from django.shortcuts import render
from .models import Cab
from django.views.generic import ListView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import *
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
				names=['DEPARTAMENTO_MUNICIPIO','PERSON_ID','CICLO','CONVENIO','TIPO_DOC','DOCUMENTO','APELLIDOS','NOMBRE','SEGUNDO_NOMBRE','TIPO_BONO','FORMULARIO','FECHA_EXPEDICION','FECHA_VENCIMIENTO','FECHA_CADUCIDAD','VALOR','SCOPE_ACCOUNT','SCOPE_PAYMENT_ST','SCOPE_PAYMENT_DT'],sheet_name='Sheet1')
				df.keys()
				sql="INSERT INTO cab_cab(departamento_municipio,person_id,ciclo,convenio,tipo_doc,documento,apellidos,nombre,segundo_nombre,tipo_bono,formulario,fecha_expedicion,fecha_vencimiento,fecha_caducidad,valor,scope_account,scope_payment_st,scope_payment_dt) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
				for i in range(len(df)):
					cursor.execute(sql,[df['DEPARTAMENTO_MUNICIPIO'][i],df['PERSON_ID'][i],df['CICLO'][i],df['CONVENIO'][i],df['TIPO_DOC'][i],df['DOCUMENTO'][i],df['DOCUMENTO'][i],df['APELLIDOS'][i],df['NOMBRE'][i],df['SEGUNDO_NOMBRE'][i],df['TIPO_BONO'][i],df['FORMULARIO'][i],df['FECHA_EXPEDICION'][i],df['FECHA_VENCIMIENTO'][i],df['FECHA_CADUCIDAD'][i],df['VALOR'][i],df['SCOPE_ACCOUNT'][i],df['SCOPE_PAYMENT_ST'][i],df['SCOPE_PAYMENT_DT'][i]])
					connection.commit()
		finally:
			connection.close()
		return redirect('cab:index-archivo')
	return render(request,'CAB/upload.html', {'form':form})