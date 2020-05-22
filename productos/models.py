from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=300, blank=False)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    existencia = models.IntegerField()
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion