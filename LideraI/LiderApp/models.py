from django.db import models

# Create your models here.

#ACTIVIDAD - MODELO PARA LA INSCRIPCION A WEBINARS - No pude cambiar el nombre de la clase 
#webinar -- Indicaría el webinar de interés (Depronto haya posibilidad de poner listas?)

class Actividad(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    webinar= models.CharField(max_length=50)
    

    def __str__(self) -> str:
        return self.nombre+" "+ self.webinar


class Lider(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email= models.EmailField()
    profesion = models.CharField(max_length=20)
    enfoque = models.CharField(max_length=30)
    #LO ENTIENDO COMO UNA SUSCRIPCION AL NEWSLETTER.
    #COMO HACER SEGUIMIENTO DE LAS PERSONAS INTERESADAS EN EL BLOG.

class Participantes(models.Model):
    nombre = models.CharField(max_length=20)
    apeliido = models.CharField(max_length=20)
    profesion = models.CharField(max_length=20)
    busqueda = models.CharField(max_length=30)