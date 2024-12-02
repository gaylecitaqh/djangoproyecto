from django.db import models
from .validators import validar_par
from .validators import validar_poliza
from .validators import validar_precio

from django.core.validators import EmailValidator

# Create your models here.

class Cliente(models.Model):
    #idcliente = models.IntegerField()

   # idcliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    #direccion = models.CharField(max_length=50)
    #telefono = models.IntegerField()

#indico como quiero que se desplieguen los datos, se ve el dato insertado

    def __str__(self):
        return self.nombre

class TipoEstados(models.TextChoices):
    PE ='p', 'Pendiente'
    CO ='c','Concluido'
    AN ='a', 'Anulado'

class Poliza(models.Model):
    numpoliza = models.CharField(max_length=100,validators=[validar_poliza,])
    moneda = models.CharField(max_length=1)
   # idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_par,validar_precio,])
    estado = models.CharField(max_length=1,choices=TipoEstados.choices, default=TipoEstados.PE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.numpoliza

class Coberturas(models.Model):
    idcobertura = models.IntegerField()
    nombrecob = models.TextField()
    estadocob = models.BooleanField(default=True)

class ObjetoAsegurado(models.Model):
    idobjeto = models.IntegerField()
    numpoliza = models.ForeignKey(Poliza, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    placa = models.CharField(max_length=10)
    