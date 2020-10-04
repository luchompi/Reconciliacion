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

    def __str__(self):
        return '{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19}'.format(self.departamento_municipio, self.person_id, self.ciclo, self.convenio, self.tipo_doc, self.documento,
self,apellidos, self.mombre, self.segundo_nombre, self.tipo_bono, self.formunario, self.fecha_expedicion,
self.fecha_vencimiento, self.fecha_caducidad, self.valor, self.scope_account, self.scope_payment_st, 
self.scope_payment_dt, self.timestamps)


    def __unicode__(self):
        return 
