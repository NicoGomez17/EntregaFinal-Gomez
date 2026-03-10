"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from futbol import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.listar_equipos, name='inicio'),
    
    
    path('equipos/', views.listar_equipos, name='equipos'),
    path('equipos/crear/', views.crear_equipo, name='crear_equipo'),
    path('equipos/editar/<int:id>/', views.editar_equipo, name='editar_equipo'),
    path('equipos/eliminar/<int:id>/', views.eliminar_equipo, name='eliminar_equipo'),

    
    path('jugadores/', views.listar_jugadores, name='jugadores'),
    path('jugadores/crear/', views.crear_jugador, name='crear_jugador'),
    path('jugadores/editar/<int:id>/', views.editar_jugador, name='editar_jugador'),
    path('jugadores/eliminar/<int:id>/', views.eliminar_jugador, name='eliminar_jugador'),

    
    path('noticias/', views.listar_noticias, name='noticias'),
    path('noticias/crear/', views.crear_noticia, name='crear_noticia'),
    path('noticias/editar/<int:id>/', views.editar_noticia, name='editar_noticia'),
    path('noticias/eliminar/<int:id>/', views.eliminar_noticia, name='eliminar_noticia'),

    
    path('about/', views.about, name='about'),

]
