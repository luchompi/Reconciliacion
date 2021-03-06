from django.db import models

# Create your models here.
class Cab(models.Model):
    departamento_municipio = models.CharField(max_length=50)
    person_id = models.CharField(max_length=255)
    ciclo = models.BigIntegerField()
    convenio = models.BigIntegerField()
    tipo_doc = models.CharField(max_length=255)
    documento = models.BigIntegerField()
    apellidos = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    segundo_nombre = models.CharField(max_length=255)
    tipo_bono = models.CharField(max_length=255)
    formulario = models.BigIntegerField()
    fecha_expedicion = models.CharField(max_length=255)
    fecha_vencimiento = models.CharField(max_length=255)
    fecha_caducidad = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
    scope_account = models.CharField(max_length=255)
    scope_payment_st = models.CharField(max_length=255)
    scope_payment_dt = models.CharField(max_length=255)
    timestamps = models.DateTimeField(auto_now=True)

class ImportarCAB(models.Model):
    nombre_archivo = models.CharField(max_length=50)
    file_name=models.FileField(upload_to='excel')
    timestamp = models.DateField(auto_now=True)
    subido = models.BooleanField(default=False)

    