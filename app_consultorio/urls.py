from django.contrib import admin
from django.urls import path , include


from .views import (    
    PacienteListView,   
    PacienteDetailView,
    PacienteCreateView,
    PacienteUpdateView,
    PacienteDeleteView,
)

app_name = "paciente"

urlpatterns = [
    path("", PacienteListView.as_view(), name="all"),
    path("create/", PacienteCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", PacienteDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", PacienteUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", PacienteDeleteView.as_view(), name="delete")

]

# -> a la urls.py del proyecto