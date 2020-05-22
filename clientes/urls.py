"""Clientes URLs."""

# Django
from django.urls import path

# Views
from clientes import views

urlpatterns = [

    path(
        route='',
        view=views.ClientsViewDetail.as_view(),
        name='detail'
    ),

    path(
        route='nuevo/',
        view=views.CreateClientsNew.as_view(),
        name='create'
    ),
    path(
        route='editar/<int:pk>',
        view = views.EditClientView.as_view(),
        name='edit'        
    ),
    path(
        route ='eliminar/<int:pk>',
        view = views.DeleteClientView.as_view(),
        name='delete'
    )
]