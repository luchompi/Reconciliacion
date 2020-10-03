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
    timestamp = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13}'.format(self.departamento,
        	self.municipio, self.serial, self.numeroConvenio, self.convenio, self.tipo_doc,self.documento,
        	self.nombre,self.tipo_bono,self.formulario,self.fecha_expedicion,self.fecha_vencimiento,
        	self.fecha_caducidad, self.valor, self.timestamp)

