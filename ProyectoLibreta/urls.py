"""
URL configuration for ProyectoLibreta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from entradaDeNota import views as entradaDeNota_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formulario/', entradaDeNota_views.formulario, name='formulario'),
    path('guardar-formulario/', entradaDeNota_views.guardar_formulario, name='guardar')
]


"""
    path('', entradaDeNota_views.index, name='index'),
    path('iniciarSesion/', entradaDeNota_views.iniciar_sesion, name='iniciarSesion'),
    path('iniciarSesion/<int:redirigir>/', entradaDeNota_views.iniciar_sesion, name='iniciarSesion'),
    path('contacto/', entradaDeNota_views.contacto, name='contacto'),
    path('contacto/<str:nombre>/', entradaDeNota_views.contacto, name='contacto'),
    path('contacto/<str:nombre>/<str:apellido>', entradaDeNota_views.contacto, name='contacto')

"""