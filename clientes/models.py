from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=250, blank=False)
    direccion = models.CharField(max_length=350)
    telefono = models.IntegerField()
    nit = models.IntegerField(unique=True, blank=False)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre
    