from django.contrib import admin
from .models import Horario, Bloque, Profesor

# Register your models here.

class HorarioAdmin(admin.ModelAdmin):
    list_display = [('nombre')]

class BloqueAdmin(admin.ModelAdmin):
    list_display = ('nombre','h_inicio','h_fin')

class ProfeAdmin(admin.ModelAdmin):
    list_display = ('usuario','nombres','apellidos','dias_disp')


admin.site.register(Profesor, ProfeAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Bloque, BloqueAdmin)
