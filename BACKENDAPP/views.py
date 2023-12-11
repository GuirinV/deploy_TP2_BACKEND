from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = "index.html"

class PacientesPage(TemplateView):
    template_name = "pacientes.html"

class ContactoPage(TemplateView):
    template_name = "contacto.html"

class Quienes_somosPage(TemplateView):
    template_name = "quienes_somos.html"