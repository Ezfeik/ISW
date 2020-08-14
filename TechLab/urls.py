from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('menu/pacientes/', views.pacientes, name='pacientes'),
    path('menu/pacientes/registrar/', views.registrar, name='registrar'),
    path('menu/pacientes/editar/<int:paciente_id>/', views.editar, name='editar'),
    path('menu/pacientes/<int:paciente_id>/', views.generarOrden, name='generarOrden')
]
