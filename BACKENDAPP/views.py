from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = "index.html"

class PacientesPage(TemplateView):
    template_name = "pacientes.html"