from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.publicacion_lista, name='publicacion_lista'),
    path('publicacion/<int:pk>', views.publicacion_detalle, name='publicacion_detalle'),
]