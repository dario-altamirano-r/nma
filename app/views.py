from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *

# Create your views here.
#--------------------------------------------------------------------------
#FUNCIONES USUARIOS
#--------------------------------------------------------------------------
def home(request):
    return render(request, 'home.html')

def inicioSesion(request):
    return render(request, 'inicioSesion.html')

def inicioSesionAdmin(request):
    return render(request, 'inicioSesionAdmin.html')

#login
def login(request):
    if request.method == "POST":
        rut = request.POST.get('rut')
        contrasena = request.POST.get('contrasena')
        origen = request.POST.get('origen')
        print(origen)

        if origen == '1': 
            user = Cliente.objects.filter(rut=rut, contrasena=contrasena).exists()
            if user:
                return HttpResponseRedirect('/homeCliente')
            else:
                return HttpResponse("Porfavor, verifica tus credenciales")


        elif origen == '2':
            user = Administrador.objects.filter(rut=rut, contrasena=contrasena).exists()
            if user:
                return HttpResponseRedirect('/homeAdmin')
            else:
                return HttpResponse("Porfavor, verifica tus credenciales")
        else:
            return render(request, 'inicioSesion.html', {})
    return render(request, 'inicioSesion.html')

#logout
def user_logout(request):
    logout(request)
    return redirect('home')

#--------------------------------------------------------------------------
#FUNCIONES ADMINISTRADOR
#--------------------------------------------------------------------------
def homeAdmin(request):
    return render(request, 'admin/homeAdmin.html')

#---------------------------------------------------------------------------

#vista profesionales
def verProfesionales(request):
    profesionales = Profesional.objects.all()
    return render(request, 'admin/verProfesionales.html', {'listaProfesionales' : profesionales})

#accion de registrar en bd
def registrarProfesional(request):
    if request.method == "POST":
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Profesional agregado exitosamente!')
            return HttpResponseRedirect('homeAdmin/verProfesionales')
    else:
        form = ClienteForm()
        return render(request, 'admin/verProfesionales.html', {'form': form})

#accion de editar profesional
def editarProfesional(request, rutProfesional):
    profesional = Profesional.objects.get(rut=rutProfesional)
    if request.method == "POST":
        form = ProfesionalForm(request.POST, instance=profesional)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Profesional actualizado exitosamente!')
            return HttpResponseRedirect('verProfesionales')
    else:
        form = ProfesionalForm(instance=profesional)
    return render(request, 'admin/editarProfesional.html', {'profesional': form})

#accion de desactivar profesional
def eliminarProfesional(request, rutProfesional):
    profesional = Profesional.objects.get(rut=rutProfesional)
    if request.method == "POST":
        profesional.estado = 0
        messages.success(request, 'Profesional actualizado exitosamente!')
        return HttpResponseRedirect('verProfesionales')
    else:
        form = ProfesionalForm(instance=profesional)
    return render(request, 'admin/editarProfesional.html', {'profesional': form})


#ver clientes
def verClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'admin/verClientes.html', {'listaClientes': clientes})

#accion de registrar en bd
def registrarCliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Cliente agregado exitosamente!')
            return HttpResponseRedirect('homeAdmin/verClientes')
    else:
        form = ClienteForm()
        return render(request, 'admin/verClientes.html', {'form': form})

#accion de editar cliente
def editarCliente(request, rutCliente):
    cliente = Cliente.objects.get(rut=rutCliente)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Cliente actualizado exitosamente!')
            return HttpResponseRedirect('homeAdmin/verClientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'admin/editarCliente.html', {'cliente': form})

#accion de eliminar cliente
def eliminarCliente(request, rutCliente):
    cliente = Cliente.objects.get(rut=rutCliente)
    if request.method == "POST":
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente!')
        return redirect('homeAdmin/verClientes')
    return render(request, 'admin/verClientes.html', {'cliente': cliente})

#accion de editar en bd
"""def editaCliente(request, rutCliente):
    cliente = Cliente.objects.get(rut=rutCliente)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Cliente actualizado exitosamente!')
            return HttpResponseRedirect('verClientes')
    else:
        form = ClienteForm(instance=cliente)
        return render(request, 'admin/registroCliente.html', {'form': form})"""


#ver visitas
def verVisitas(request):
    clientes = Cliente.objects.all()
    profesionales = Profesional.objects.all()
    visitas = Visita.objects.all()
    return render(request, 'admin/verVisitas.html', {'listaVisitas': visitas, 'listaClientes': clientes, 'listaProfesionales': profesionales})

#accion de registrar en bd
def registrarVisita(request):
    if request.method == "POST":
        form = VisitaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Visita agregado exitosamente!')
            return HttpResponseRedirect('homeAdmin/verVisitas')
    else:
        form = VisitaForm()
        return render(request, 'admin/verVisitas.html', {'form': form})

#accion de editar cliente
def editarVisita(request, id):
    visita = Visita.objects.get(id=id)
    if request.method == "POST":
        form = VisitaForm(request.POST, instance=visita)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Visita actualizada exitosamente!')
            return HttpResponseRedirect('homeAdmin/verVisitas')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'admin/editarCliente.html', {'visita': form})

#accion de eliminar visita
def eliminarVisita(request, id):
    visita = Visita.objects.get(id=id)
    if request.method == "POST":
        visita.delete()
        messages.success(request, 'Cliente eliminado exitosamente!')
        return redirect('homeAdmin/verVisitas')
    return render(request, 'admin/verVisitas.html')


#seccion material
def verMateriales(request):
    return render(request, 'admin/verMateriales.html')


#seccion fiscalizaciones
def verFiscalizaciones(request):
    fiscalizaciones = Chequeo.objects.all()
    return render(request, 'admin/verFiscalizaciones.html', {'listaFiscalizaciones': fiscalizaciones})


#seccion capacitaciones
def verCapacitaciones(request):
    capacitaciones = Capacitacion.objects.all()
    return render(request, 'admin/verCapacitaciones.html', {'listaCapacitaciones': capacitaciones})


#seccion calendario
def verCalendario(request):
    visitas = Visita.objects.all()
    return render(request, 'admin/verCalendario.html', {'listaVisitas': visitas})


#seccion finanzas
def verFinanzas(request):
    pagos = Pago.objects.all()
    return render(request, 'admin/verFinanzas.html', {'listaPagos': pagos})


#seccion solicitudes
def verSolicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'admin/verSolcitudes.html', {'listaSolicitudes': solicitudes})


#--------------------------------------------------------------------------
#FUNCIONES CLIENTE
#--------------------------------------------------------------------------
def homeCliente(request):
    return render(request, 'cliente/homeCliente.html')

def verMaterialCliente(request):
    return render(request, 'cliente/verMaterialesCliente.html')

def verFiscalizacionesCliente(request):
    return render(request, 'cliente/verFiscalizacionesCliente.html')

def verCapacitacionesCliente(request):
    return render(request, 'cliente/verCapacitacionesCliente.html')

def verCalendarioCliente(request):
    return render(request, 'cliente/verCalendarioCliente.html')

def verFinanzasCliente(request):
    return render(request, 'cliente/verFinanzasCliente.html')

def verSolicitudesCliente(request):
    return render(request, 'cliente/verSolicitudesCliente.html')

#--------------------------------------------------------------------------
#FUNCIONES PROFESIONAL
#--------------------------------------------------------------------------
def homeProfesional(request):
    return render(request, 'profesional/homeProfesional.html')

