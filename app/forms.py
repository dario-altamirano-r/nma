from django.forms import ModelForm
from .models import *

class AdministradorForm(ModelForm):
    class Meta:
        model = Administrador
        fields = ['rut','email','contrasena']

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut','nombreEmpresa','email','rubro','tamanio','mutualidad','numeroTelefono','contrasena','estado']


class ProfesionalForm(ModelForm):
    class Meta:
        model = Profesional
        fields = ['rut','nombreCompleto','email','categoria','contrasena','estado']

class VisitaForm(ModelForm):
    class Meta:
        model = Visita
        fields = ['rutCliente','rutProfesional','fecha','observaciones','recomendaciones']