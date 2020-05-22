from django import forms
from clientes.models import Clientes

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre','direccion','telefono','nit']