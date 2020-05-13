from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
# Create your views here.

from clientes.forms import ClientesForm

# Models
from clientes.models import Clientes

class CreateClientsNew(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'clientes/new.html'
    form_class = ClientesForm
    success_url = reverse_lazy('clientes:detail')



class ClientsViewDetail(LoginRequiredMixin, ListView):
    """Return post detail."""

    template_name = 'clientes/detail.html'
    model = Clientes
    ordering = ('-fechaCreacion',)
    context_object_name = 'clients'


class EditClientView(LoginRequiredMixin,UpdateView):
    template_name = 'clientes/editar.html'
    model = Clientes
    success_url = reverse_lazy('clientes:detail')
    fields = ['direccion','telefono','estado']
    ##fields = "__all__"

class DeleteClientView(DeleteView):
    template_name = 'clientes/confirmacioneliminacion.html'
    model = Clientes    
    success_url = reverse_lazy('clientes:detail')
