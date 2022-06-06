from django.urls import path
from LiderApp.views import *

urlpatterns = [
    path ('actividad/', actividad),
    path ('actividades/', actividades),
    path ('lideres/', lideres),
    path ('', inicio),
    path('comunidad/',comunidad, name="comunidad"),
    path('masterclass/',masterclass, name="masterclass"),
    path('principios/',principios, name="principios"),
]