
# Create your views here.


from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Paciente

# Create your views here.


class PacienteBaseView(View):
    template_name = 'paciente.html'
    model = Paciente
    fields = '__all__'
    success_url = reverse_lazy('paciente:all')


class PacienteListView(PacienteBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS paciente
    """

class PacienteDetailView(PacienteBaseView,DetailView):
    template_name = "paciente_detail.html"

class PacienteCreateView(PacienteBaseView,CreateView):
    template_name = "paciente_create.html"
    extra_context = {"tipo": "Crear paciente"}


class PacienteUpdateView(PacienteBaseView,UpdateView):
    template_name = "paciente_create.html"
    extra_context = {"tipo": "Actualizar paciente"}

class PacienteDeleteView(PacienteBaseView,DeleteView):
    template_name = "paciente_delete.html"
    extra_context = {"tipo": "Borrar paciente"}

# -> app_consultorio.urls.py