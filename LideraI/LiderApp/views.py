from django.http import HttpResponse
from django.shortcuts import render
from LiderApp.models import Actividad, Lider
from django.template import loader
from LiderApp.forms import *

# Create your views here.

def actividad(self):
    actividad= Actividad(nombre="ConociendoME", participantes= '10')
    actividad.save()
    documento = f"Actividad: {actividad.nombre} - Participantes: {actividad.participantes}"
    return HttpResponse(documento)

def lideres(request):
        return render(request, "liderapp/lideres.html")

def actividades(request):
        return render(request, "liderapp/actividades.html")

def inicio(self):
    plantilla = loader.get_template('LiderApp/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def masterclass(request):
        if request.method=="POST":
                lider_formulario= LiderFormulario(request.POST)
                print(lider_formulario)
                
                if lider_formulario.is_valid():
                        informacion= lider_formulario.cleaned_data
                        nombre= request.POST['nombre']
                        apellido= request.POST['apellido']
                        email= request.POST['email']
                        profesion= request.POST['profesion']
                        enfoque= request.POST['enfoque']
                        lider= Lider(nombre=nombre, apellido=apellido, email=email, profesion=profesion, enfoque=enfoque)
                        lider.save()
                        return render(request, "LiderApp/inicio.html")
        else:
                lider_formulario=LiderFormulario()
        return render(request, "MasterClass/masterclass.html", {'lider_formulario':lider_formulario})