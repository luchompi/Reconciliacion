from django.db import models

# Create your models here.
class Cab(models.Model):
    departamento_municipio = models.CharField(max_length=50)
    person_id = models.CharField(max_length=50)
    ciclo = models.IntegerField()
    convenio = models.IntegerField()
    tipo_doc = models.CharField(max_length=50)
    documento = models.IntegerField(primary_key=True,unique=False)
    apellidos = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    tipo_bono = models.CharField(max_length=50)
    formulario = models.IntegerField()
    fecha_expedicion = models.CharField(max_length=50)
    fecha_vencimiento = models.CharField(max_length=50)
    fecha_caducidad = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    scope_account = models.CharField(max_length=50)
    scope_payment_st = models.CharField(max_length=50)
    scope_payment_dt = models.CharField(max_length=50)
    timestamps = models.DateTimeField(auto_now=True)

class ImportarCAB(models.Model):
    nombre_archivo = models.CharField(max_length=50)
    file_name=models.FileField(upload_to='excel')
    timestamp = models.DateField(auto_now=True)
    subido = models.BooleanField(default=False)

    