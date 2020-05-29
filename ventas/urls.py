from django.urls import path, include

from .views import FacturaView, facturas, ProductoView

from ventas.reportes import imprimir_venta



urlpatterns = [
    path('',FacturaView.as_view(),name='venta_list'),
    path('new/',facturas,name='venta_new'),
    path('buscar-producto/',ProductoView.as_view(), name="venta_producto"),
    path('edit/<int:id>',facturas, name="venta_edit"),
    path('<int:id>/imprimir',imprimir_venta, name="venta_imprimir_one"),
]
