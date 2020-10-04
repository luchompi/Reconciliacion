from django.db import models

# Create your models here.
class Paf(models.Model):
    departamento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    numeroConvenio = models.CharField(max_length=50)
    convenio = models.CharField(max_length=50)
    tipo_doc = models.CharField(max_length=50)
    documento = models.IntegerField(primary_key=True, unique=False)
    nombre = models.CharField(max_length=250)
    tipo_bono = models.CharField(max_length=50)
    formulario = models.CharField(max_length=50)
    fecha_expedicion = models.CharField(max_length=50)
    fecha_vencimiento = models.CharField(max_length=50)
    fecha_caducidad = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    timestamps = models.DateTimeField(auto_now_add=True)
  
class ImportarPAF(models.Model):
      
    file_name=models.FileField(upload_to='excel')
    timestamp = models.DateField(auto_now=True)
    subido = models.BooleanField(default=False)

    

    def __str__(self):
        return f"File id: {self.id}"

    def __unicode__(self):
        return 
