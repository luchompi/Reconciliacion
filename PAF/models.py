from django.db import models

# Create your models here.
class PAF(models.Model):
    departamento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    numeroConvenio = models.CharField(max_length=50)
    convenio = models.CharField(max_length=50)
    tipo_doc = models.CharField(max_length=50)
    documento = models.IntegerField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=250)
    tipo_bono = models.CharField(max_length=50)
    formulario = models.CharField(max_length=50)
    fecha_expedicion = models.CharField(max_length=50)
    fecha_vencimiento = models.CharField(max_length=50)
    fecha_caducidad = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now=True)
  
    def __str__(self):

        return 

    def __unicode__(self):
        return 
