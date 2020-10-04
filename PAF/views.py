from django.shortcuts import render
from .forms import ExcelModelForm
import xlrd
from .models import ImportarPAF
from django.db import connection
# Create your views here.
def upload(request):
	form = ExcelModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.name="excel"
		form.save()
		form = ExcelModelForm
		cursor = connection.cursor()
		cursor.execute('''SELECT file_name FROM  PAF_IMPORTARPAF WHERE  EXTRACT(HOUR FROM SYSDATE)  ''')
		row = cursor.fetchone()
		
		book = xlrd.open_workbook(row)
		print("The number of worksheets is {0}".format(book.nsheets))
		print("Worksheet name(s): {0}".format(book.sheet_names()))
		sh = book.sheet_by_index(0)
		print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
		print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
		for rx in range(sh.nrows):
			print(sh.row(rx))


	return render(request,'PAF/upload.html', {'form':form})




def index(request):
	return render(request,'PAF/index.html')
