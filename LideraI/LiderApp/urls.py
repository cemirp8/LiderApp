from django.urls import path
from LiderApp.views import actividad, actividades, lideres, inicio

urlpatterns = [
    path ('actividad/', actividad),
    path ('actividades/', actividades),
    path ('lideres/', lideres),
    path ('', inicio),
]