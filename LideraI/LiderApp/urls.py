from django.urls import path
from LiderApp.views import actividad

urlpatterns = [
    path('actividad/', actividad),
]