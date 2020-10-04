from django.urls import path
from . import views

app_name="autor"

urlpatterns = [
    path('', views.index, name='index'),
    #path('nuevo/', views.autor_view(), name='autor_crear'),
]
