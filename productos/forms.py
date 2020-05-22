from django import forms
from productos.models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        #fields = '__all__'
        fields = ['descripcion','costo','precio','existencia']
