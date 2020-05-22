"""Compras URLs."""

# Django
from django.urls import path

# View
# from compras import views

from .views import index, compras, ComprasView, CompraDetDelete

urlpatterns = [

    path(
        route='',
        view=ComprasView.as_view(),
        name='compras_list'
    ),
    path('new/',compras, name="compras_new"),
    path('edit/<int:compra_id>',compras, name="compras_edit"),    
    path('compras/<int:compra_id>/delete/<int:pk>',CompraDetDelete.as_view(), name="compras_del"),

]