from django.http import HttpResponse
from django.shortcuts import render
from LiderApp.models import Actividad

from django.template import loader
# Create your views here.

def actividad(self):
    actividad= Actividad(nombre="ConociendoME", participantes= '10')
    actividad.save()
    documento = f"Actividad: {actividad.nombre} - Participantes: {actividad.participantes}"
    return HttpResponse(documento)