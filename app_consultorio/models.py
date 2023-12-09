from django.db import models
from django.db.models import Model

# Create your models here.

class Paciente(Model):
    """
    Atributos de clase que son usadas por herencia de la clase Model

    """
    nombre_appellido  =  models.CharField(max_length=100,default="Desconocido")
    direccion  =  models.CharField(max_length=100)
    mail  =  models.EmailField(blank=False,null=False,default="no_email_contact@gmail.com")
    edad  = models.PositiveSmallIntegerField(blank=False,null=False)
    telefono  =  models.CharField(max_length=20)
    peso  = models.FloatField(blank=True, null=True)
    alta_paciente  = models.DateField(auto_now=True)

    # podemos crear la tabla con un nombre especifico pero se lo tenemos
    # que indicar directamente en la metaclase

    class Meta:
        db_table = "consultorio_del_Dr"


    def __str__(self):
        return f"El Paciente: {self.}, edad {self.edad}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
    
    # -> paso siguiente -> admin.py

