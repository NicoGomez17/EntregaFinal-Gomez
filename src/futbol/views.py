from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo, Jugador, Noticia
from .forms import EquipoForm, JugadorForm, NoticiaForm


def listar_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'futbol/equipos.html', {'equipos': equipos})


def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos')
    else:
        form = EquipoForm()
    return render(request, 'futbol/crear_equipo.html', {'form': form})


def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('equipos')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'futbol/crear_equipo.html', {'form': form})


def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    equipo.delete()
    return redirect('equipos')








def listar_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'futbol/jugadores.html', {'jugadores': jugadores})


def crear_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jugadores')
    else:
        form = JugadorForm()
    return render(request, 'futbol/crear_jugador.html', {'form': form})


def editar_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    if request.method == 'POST':
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('jugadores')
    else:
        form = JugadorForm(instance=jugador)
    return render(request, 'futbol/crear_jugador.html', {'form': form})


def eliminar_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    jugador.delete()
    return redirect('jugadores')







def listar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'futbol/noticias.html', {'noticias': noticias})


def crear_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('noticias')
    else:
        form = NoticiaForm()
    return render(request, 'futbol/crear_noticia.html', {'form': form})


def editar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticias')
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'futbol/crear_noticia.html', {'form': form})

def eliminar_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    noticia.delete()
    return redirect('noticias')








def about(request):
    return render(request, 'futbol/about.html')