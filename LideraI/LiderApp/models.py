from django.db import models

# Create your models here.
class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    participantes = models.IntegerField()

#virtual = models.BooleanField()

class Lider(models.Model):
    nombre = models.CharField(max_length=20)
    apeliido = models.CharField(max_length=20)
    profesion = models.CharField(max_length=20)
    enfoque = models.CharField(max_length=30)

class Participantes(models.Model):
    nombre = models.CharField(max_length=20)
    apeliido = models.CharField(max_length=20)
    profesion = models.CharField(max_length=20)
    busqueda = models.CharField(max_length=30)