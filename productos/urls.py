"""
URLS para productos
"""

from django.urls import path
from productos import views

urlpatterns = [
    path(
        route = '',
        view = views.ProductsDetailView.as_view(),
        name='detail'
    ),
    path(
        route = 'nuevo',
        view = views.ProductsCreateView.as_view(),
        name='new'
    ),
    path(
        route = 'editar/<int:pk>',
        view = views.ProductEditView.as_view(),
        name = 'edit'
    )
]
