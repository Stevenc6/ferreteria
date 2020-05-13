"""Compras views."""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView, ListView
from django.contrib.auth import views as auth_views

# Models
from django.contrib.auth.models import User



# Forms
from users.forms import SignupForm



    



class WelcomeView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    """
    template_name = 'users/index.html'
    model = none
    """
    pass


