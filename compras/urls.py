"""Compras URLs."""

# Django
from django.urls import path

# View
from compras import views


urlpatterns = [

    path(
        route='',
        view=views.WelcomeView.as_view(),
        name='feed'
    )

]