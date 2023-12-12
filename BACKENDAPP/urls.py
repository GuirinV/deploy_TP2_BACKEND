"""
URL configuration for BACKENDAPP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from .views import IndexPage
from .views import PacientesPage,ContactoPage,Quienes_somosPage,PerdisteContraseñaPage,RegistrarsePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPage.as_view(), name="index"),
    path('pacientes', PacientesPage.as_view(), name="pacientes"),
    path("paciente/", include("app_consultorio.urls")),
    path('contacto', ContactoPage.as_view(), name="contacto"),
    path('quienes_somos', Quienes_somosPage.as_view(), name="quienes_somos"),

    path('perdisteContraseña', PerdisteContraseñaPage.as_view(), name="perdisteContraseña"),
    path('registrarse', RegistrarsePage.as_view(), name="registrarse"),

]
