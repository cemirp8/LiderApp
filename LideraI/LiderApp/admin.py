from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Actividad)
admin.site.register(Lider)
admin.site.register(Participantes)