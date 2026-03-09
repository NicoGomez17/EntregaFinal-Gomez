from django.contrib import admin

from .models import Equipo, Jugador, Noticia

admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Noticia)