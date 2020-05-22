from django import forms
from compras.models import CompraEncabezado


class ComprasEncForm(forms.ModelForm):
    fecha_compra = forms.DateInput()

    class Meta:
        model = CompraEncabezado
        fields = ['idOrdenCompra','observaciones','sub_total',
        'total']
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True



