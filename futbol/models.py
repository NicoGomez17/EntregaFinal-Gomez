from django.db import models

# Create your models here.

from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fundacion = models.IntegerField()

    def __str__(self):
        return self.nombre


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    posicion = models.CharField(max_length=50)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.titulo