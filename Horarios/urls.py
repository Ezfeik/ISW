from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('menu/pdf/', views.pdf, name='pdf'),
    path('menu/profesor/<int:profesor_id>/', views.profesor, name='profesor'),
]
