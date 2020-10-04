from django.shortcuts import render
from .forms import ExcelModelForm
# Create your views here.
def upload(request):
	form = ExcelModelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		form = ExcelModelForm
	return render(request,'PAF/upload.html', {'form':form})


def index(request):
	return render(request,'PAF/index.html')
