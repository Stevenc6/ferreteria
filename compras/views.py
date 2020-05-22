"""Compras views."""

from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
import datetime
from django.http import HttpResponse, JsonResponse

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
import json
from django.db.models import Sum

from compras.models import CompraDetalle, CompraEncabezado
from compras.forms import ComprasEncForm
# from bases.views import SinPrivilegios
from productos.models import Producto


def index(request):
    return render(request,'compras/compras.html')


class ComprasView(generic.ListView):
    model = CompraEncabezado
    template_name = "compras/compras_list.html"
    context_object_name = "obj"
    # permission_required="cmp.view_comprasenc"



@login_required(login_url='/users/login/')

def compras(request,compra_id=None):
    template_name = 'compras/compras.html'
    prod = Producto.objects.filter(estado=True)
    form_compras = {}
    contexto = {}

    if request.method=='GET':
        form_compras = ComprasEncForm()
        enc = CompraEncabezado.objects.filter(pk=compra_id).first()

        if enc:
            det = CompraDetalle.objects.filter(idCompra = enc)
            e = {
                'observaciones': enc.observaciones,
                'idOrdenCompra': enc.idOrdenCompra,
                'sub_total': enc.sub_total,
                'total': enc.total
            }
            form_compras = ComprasEncForm(e)
        else:
            det = None
                
        contexto = {'productos':prod,'encabezado':enc,'detalle':det,'form_enc':form_compras}
        print(prod)
        print(enc)

    if request.method=='POST':
        observaciones = request.POST.get("observaciones")
        idOrdenCompra = request.POST.get("idOrdenCompra")

        sub_total = 0
        total = 0

        if not compra_id:
            enc = CompraEncabezado(
                observaciones = observaciones,
                idOrdenCompra = idOrdenCompra,
                usuario = request.user
            )
            if enc:
                enc.save()
                compra_id = enc.id
        else:
            enc = CompraEncabezado.objects.filter(pk=compra_id).first()
            if enc:
                enc.observaciones = observaciones
                enc.idOrdenCompra = idOrdenCompra
                enc.save()

        if not compra_id:
            return redirect("compras:feed")


        producto = request.POST.get('id_id_producto')        
        cantidad = request.POST.get('id_cantidad_detalle')
        costo = request.POST.get('id_precio_detalle')
        sub_total_detalle = request.POST.get("id_sub_total_detalle")
        # descuento_detalle  = request.POST.get("id_descuento_detalle")
        total_detalle  = request.POST.get("id_total_detalle")
        


        prod = Producto.objects.get(pk=producto)        

        det = CompraDetalle(
            idCompra = enc,
            producto = prod,
            cantidad = cantidad,
            precio_prv=costo,            
            costo = 0
        )

        if det:
            det.save()

            sub_total=CompraDetalle.objects.filter(idCompra=compra_id).aggregate(Sum('sub_total'))
            #descuento=CompraDetalle.objects.filter(idCompra=compra_id).aggregate(Sum('descuento'))
            enc.sub_total = sub_total["sub_total__sum"]
            #enc.descuento=descuento["descuento__sum"]
            enc.save()

            return redirect('compras:compras_edit',compra_id=compra_id)

    
    return render(request,template_name,contexto)



class CompraDetDelete(generic.DeleteView):
    model = CompraDetalle
    template_name = "compras/compras_det_del.html"
    context_object_name = 'obj'
    
    def get_success_url(self):
          compra_id=self.kwargs['idCompra']
          return reverse_lazy('compras:compras_edit', kwargs={'idCompra': compra_id})


