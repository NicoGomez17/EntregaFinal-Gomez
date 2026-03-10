from django import forms
from .models import Equipo, Jugador, Noticia

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'