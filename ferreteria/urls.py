"""ferreteria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views

urlpatterns = [    
    path('admin/', admin.site.urls),
    path('',views.welcome, name="feed"),
    path('compras/', include(('compras.urls', 'compras'), namespace='compras')),
    path('clientes/', include(('clientes.urls', 'clientes'), namespace='clientes')),
    path('productos/', include(('productos.urls', 'productos'), namespace='productos')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('ventas/',include(('ventas.urls','ventas'),namespace='ventas')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
