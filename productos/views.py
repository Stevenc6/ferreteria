from django.shortcuts import render
from django.urls import reverse_lazy
from productos.models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from productos.forms import ProductoForm
# Create your views here.



class ProductsDetailView(LoginRequiredMixin, ListView):
    """Return products detail."""

    template_name = 'productos/detail.html'
    model = Producto
    ordering = ('-fechaCreacion',)
    context_object_name = 'productos'



class ProductsCreateView(LoginRequiredMixin,CreateView):
    """ Crea un nuevo producto """
    template_name = "productos/new.html"
    form_class = ProductoForm
    success_url = reverse_lazy('productos:detail')

class ProductEditView(LoginRequiredMixin,UpdateView):
    template_name = "productos/editar.html"
    model = Producto
    success_url = reverse_lazy('productos:detail')
    fields = ['precio','costo','existencia','estado']