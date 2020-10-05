from django.urls import path
from . import views

app_name="paf"

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('new_paf/', views.rowPafCreate.as_view(), name='crear_paf'),
    path('new_paf/<pk>/', views.rowPafEdit.as_view(), name='edit_paf'),
    path('del_paf/<pk>/', views.rowPafDelete.as_view(), name='del_paf'),
    path('load_file/', views.upload, name='carga'),
    path('index_file/', views.index_file.as_view(), name='index-archivo'),
    path('edit_file/<pk>/', views.update_file.as_view(), name='editar_archivo'),
    path('delete_file/<int:id>/', views.file_delete, name='eliminar_archivo'),



]
