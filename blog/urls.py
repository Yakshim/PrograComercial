from typing import ValuesView
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.publicacion_lista, name='publicacion_lista'),
    path('publicacion/<int:pk>', views.publicacion_detalle, name='publicacion_detalle'),
    path('publicacion/nueva/', views.publicacion_nueva, name='publicacion_nueva'),
    path('publicacion/<int:pk>/editar/', views.publicacion_editar, name='publicacion_editar'),
]