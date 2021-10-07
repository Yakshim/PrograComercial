from django.shortcuts import redirect ,render, get_object_or_404
from django.utils import timezone
from .models import Publicacion
from .forms import PublicacionForm
from blog import forms
from django.contrib.auth.decorators import login_required


def publicacion_lista(request):
    publicaciones= Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/publicacion_lista2.html', {'publicaciones': publicaciones})

@login_required
def publicacion_detalle(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/publicacion_detalle.html',{'publicacion':publicacion})

@login_required
def publicacion_nueva(request):
    if request.method == "POST":
        formulario = PublicacionForm(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            publicacion.fecha_publicacion = timezone.now()
            publicacion.save()
            return redirect('publicacion_detalle', pk=publicacion.pk)
    else:
        formulario = PublicacionForm()        
    return render(request, 'blog/publicacion_editar.html', {'formulario': formulario})


@login_required
def publicacion_editar(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        formulario = PublicacionForm(request.POST, instance=publicacion)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            publicacion.fecha_publicacion = timezone.now()
            publicacion.save()
            return redirect('publicacion_detalle', pk=publicacion.pk)
    else:
        formulario = PublicacionForm(instance=publicacion)
    return render(request, 'blog/publicacion_editar.html', {'formulario': formulario})


@login_required
def publicacion_borrador_lista(request):
    publicaciones = Publicacion.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/publicacion_borrador_lista.html', {'publicaciones': publicaciones})

@login_required
def publicacion_publicar(request, pk):
    publicacion= get_object_or_404(Publicacion, pk=pk)
    publicacion.publicar()
    return redirect('publicacion_detalle', pk=pk)

@login_required
def publicacion_eliminar(request, pk):
    publicacion= get_object_or_404(Publicacion, pk=pk)
    publicacion.delete()
    return redirect('publicacion_lista')
# Create your views here.
