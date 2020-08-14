from django.contrib import admin
from .models import Paciente, Usuario, Orden

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','sexo','peso')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario','nombre','tipo')

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('paciente','tipo_examen','hora')

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Orden, OrdenAdmin)
