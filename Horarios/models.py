from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Horario(models.Model):
    nombre = models.CharField(max_length=20, default="Horario_de_clase" ,editable=True)
    def __str__(self):
        return self.nombre

class Bloque(models.Model):
    nombre = models.CharField(max_length=20, default='', editable=True)
    h_inicio = models.TimeField(editable=True)
    h_fin = models.TimeField(editable=True)
    horario_asignado = models.ForeignKey(Horario, on_delete=models.CASCADE, related_name="h_asig")
    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dias_disp = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return self.nombres
