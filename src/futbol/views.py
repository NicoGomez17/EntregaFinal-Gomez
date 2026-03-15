from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo, Jugador, Noticia
from .forms import EquipoForm, JugadorForm, NoticiaForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def inicio(request):
    return render(request, 'futbol/inicio.html')



def listar_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'futbol/equipos.html', {'equipos': equipos})



def listar_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'futbol/jugadores.html', {'jugadores': jugadores})





def listar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'futbol/noticias.html', {'noticias': noticias})




def about(request):
    return render(request, 'futbol/about.html')






def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()

    return render(request, 'futbol/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')

    else:
        form = AuthenticationForm()

    return render(request, 'futbol/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('inicio')