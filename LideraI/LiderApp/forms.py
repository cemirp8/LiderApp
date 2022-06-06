from django import forms

class LiderFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email= forms.EmailField()
    profesion = forms.CharField(max_length=20)
    enfoque = forms.CharField(max_length=30)