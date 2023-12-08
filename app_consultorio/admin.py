from django.contrib import admin
from django.contrib.admin import ModelAdmin 
from .models import Paciente

# Register your models here.
@admin.register(Paciente)
class PacientesAdmin(ModelAdmin):
    ...

# --> settings.py (settings del proyect)