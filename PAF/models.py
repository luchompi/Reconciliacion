from django.db import models

# Create your models here.
class Paf(models.Model):
    departamento = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    serial = models.BigIntegerField()
    numeroConvenio = models.CharField(max_length=255)
    convenio = models.BigIntegerField()
    tipo_doc = models.CharField(max_length=255)
    documento = models.BigIntegerField()
    nombre = models.CharField(max_length=255)
    tipo_bono = models.CharField(max_length=255)
    formulario = models.CharField(max_length=255)
    fecha_expedicion = models.CharField(max_length=255)
    fecha_vencimiento = models.CharField(max_length=255)
    fecha_caducidad = models.CharField(max_length=255)
    valor = models.CharField(max_length=255)
    timestamps = models.DateTimeField(auto_now_add=True)
  
class ImportarPAF(models.Model):
    nombre_archivo = models.CharField(max_length=50)
    file_name=models.FileField(upload_to='excel')
    timestamp = models.DateField(auto_now=True)
    subido = models.BooleanField(default=False)

    

    def __str__(self):
        return str(self.nombre_archivo)

    def __unicode__(self):
        return 
