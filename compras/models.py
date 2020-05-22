from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto
from decimal import *
from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete


# Create your models here.

class CompraEncabezado(models.Model):    
    #monto = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.BooleanField(default=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    idOrdenCompra = models.IntegerField(unique=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)
    sub_total=models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total=models.DecimalField(max_digits=8, decimal_places=2)


    def __str__(self):
        return '{}'.format(self.observaciones)

    def save(self):
        self.observaciones = self.observaciones.upper()
        self.total = self.sub_total 
        super(CompraEncabezado,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Compras"
        verbose_name="Encabezado Compra"


class CompraDetalle(models.Model):
    idCompra = models.ForeignKey(CompraEncabezado, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=1)    
    costo = models.DecimalField(max_digits=8, decimal_places=2)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_prv=models.DecimalField(max_digits=8, decimal_places=2)
    sub_total=models.DecimalField(max_digits=8, decimal_places=2, default=0)    
    total=models.DecimalField(max_digits=8, decimal_places=2)
    

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = Decimal(Decimal(int(self.cantidad)) * Decimal(self.precio_prv))
        self.total = self.sub_total
        super(CompraDetalle, self).save()
    
    class Mega:
        verbose_name_plural = "Detalles Compras"
        verbose_name="Detalle Compra"



@receiver(post_delete, sender=CompraDetalle)
def detalle_compra_borrar(sender,instance, **kwargs):
    id_producto = instance.producto.id
    id_compra = instance.compra.id

    enc = CompraEncabezado.objects.filter(pk=id_compra).first()
    if enc:
        sub_total = CompraDetalle.objects.filter(idCompra=id_compra).aggregate(Sum('sub_total'))
        #descuento = CompraDetalle.objects.filter(compra=id_compra).aggregate(Sum('descuento'))
        enc.sub_total=sub_total['sub_total__sum']
        # enc.descuento=descuento['descuento__sum']
        enc.save()
    
    prod=Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) - int(instance.cantidad)
        prod.existencia = cantidad
        prod.save()


@receiver(post_save, sender=CompraDetalle)
def detalle_compra_guardar(sender,instance,**kwargs):
    id_producto = instance.producto.id
    # fecha_compra=instance.compra.fecha_compra
    print(id_producto)
    prod=Producto.objects.filter(pk=id_producto).first()
    if prod:
        cantidad = int(prod.existencia) + int(instance.cantidad)
        prod.existencia = cantidad
        #prod.ultima_compra=fecha_compra
        prod.save()