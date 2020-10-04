from django.urls import path
from . import views

app_name="paf"

urlpatterns = [
    path('', views.index, name='index'),
    path('Cargar_Excell/', views.upload, name='carga'),
    path('index_file/', views.index_file.as_view(), name='index-archivo'),
    path('editar/<pk>/', views.update_file.as_view(), name='editar_archivo'),
    path('eliminar/<int:id>/', views.file_delete, name='eliminar_archivo'),



]
