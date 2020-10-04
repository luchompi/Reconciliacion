from django.urls import path
from . import views

app_name="autor"

urlpatterns = [
    path('', views.index, name='index'),
    path('Cargar_Excell/', views.upload, name='carga'),
]
