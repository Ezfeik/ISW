from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Paciente(models.Model):
    rut = models.CharField(max_length=9, default='', unique=True)
    nombre = models.CharField(max_length=20, default='', editable=True)
    edad = models.IntegerField(default=1)
    sexo = models.CharField(max_length=20, default='')
    peso = models.IntegerField(default=1)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, default="Horario_de_clase" ,editable=True)
    tipo = models.IntegerField(default=1)
    def __str__(self):
        return self.nombre

class Orden(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_examen = models.CharField(max_length=100)
    hora = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.tipo_examen
