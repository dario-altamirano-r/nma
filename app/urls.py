from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [

    #redireccionamiento
    path('', lambda req:redirect('home')),

    #vista home
    path('home/', views.home, name = 'home'),

    #vista de inicio de sesion
    path('inicioSesion/', views.inicioSesion, name = 'inicioSesion'),
    path('inicioSesionAdmin/', views.inicioSesionAdmin, name = 'inicioSesionAdmin'),

    #accion de logueo
    path('login/', views.login, name = 'login'),

    #cerrar sesion
    path('logout', views.user_logout, name = 'logout'),

#-----------------------------------------------------------------------------------------#
    #PANEL ADMINISTRADOR
    #home
    path('homeAdmin/', views.homeAdmin, name = 'homeAdmin'),

    #seccion profesionales
    #path('registroProfesional/', views.registroProfesional, name = 'registroProfesional'),
    path('homeAdmin/verProfesionales/', views.verProfesionales, name = 'verProfesionales'),
    path('registrarProfesional', views.registrarProfesional, name = 'registrarProfesional'),
    path('editarProfesional/<str:rutProfesional>', views.editarProfesional, name='editarProfesional'),
    path('eliminarProfesional/<str:rutProfesional>', views.eliminarProfesional, name='eliminarProfesional'),

    #seccion clientes
    #path('registroCliente/', views.registroCliente, name = 'registroCliente'),
    path('homeAdmin/verClientes/', views.verClientes, name = 'verClientes'),
    path('registrarCliente', views.registrarCliente, name = 'registrarCliente'),
    path('editarCliente/<str:rutCliente>', views.editarCliente, name='editarCliente'),
    path('eliminarCliente/<str:rutCliente>', views.eliminarCliente, name='eliminarCliente'),

    #seccion visitas
    path('homeAdmin/verVisitas/', views.verVisitas, name = 'verVisitas'),
    path('registrarVisita', views.registrarVisita, name = 'registrarVisita'),
    path('editarVisita/<int:id>', views.editarVisita, name='editarVisita'),
    path('eliminarVisita/<int:id>', views.eliminarVisita, name='eliminarVisita'),

    #seccion material
    path('homeAdmin/verMateriales/', views.verMateriales, name = 'verMateriales'),

    #seccion fiscalizaciones
    path('homeAdmin/verFiscalizaciones/', views.verFiscalizaciones, name = 'verFiscalizaciones'),

    #seccion capacitaciones
    path('homeAdmin/verCapacitaciones/', views.verCapacitaciones, name = 'verCapacitaciones'),

    #seccion calendario
    path('homeAdmin/verCalendario/', views.verCalendario, name = 'verCalendario'),

    #seccion finanzas
    path('homeAdmin/verFinanzas/', views.verFinanzas, name = 'verFinanzas'),

    #seccion solicitudes
    path('homeAdmin/verSolicitudes/', views.verSolicitudes, name = 'verSolicitudes'),


#-----------------------------------------------------------------------------------------#
    #PANEL CLIENTE

    #home
    path('homeCliente/', views.homeCliente, name = 'homeCliente'),

    #seccion material
    path('homeCliente/verMaterialesCliente/', views.verMaterialCliente, name = 'verMaterialesCliente'),

    #seccion fiscalizaciones
    path('homeCliente/verFiscalizacionesCliente/', views.verFiscalizacionesCliente, name = 'verFiscalizacionesCliente'),

    #seccion capacitaciones
    path('homeCliente/verCapacitacionesCliente/', views.verCapacitacionesCliente, name = 'verCapacitacionesCliente'),

    #seccion calendario
    path('homeCliente/verCalendarioCliente/', views.verCalendarioCliente, name = 'verCalendarioCliente'),

    #seccion finanzas
    path('homeCliente/verFinanzasCliente/', views.verFinanzasCliente, name = 'verFinanzasCliente'),

    #seccion solicitudes
    path('homeCliente/verSolicitudesCliente/', views.verSolicitudesCliente, name = 'verSolicitudesCliente'),

#-----------------------------------------------------------------------------------------#

    #vista de profesional
    path('homeProfesional/', views.homeProfesional, name = 'homeProfesional'),

    #establecer fecha de disponibilidad
    #aqui es donde el profesional debe indicar su fechas disponibles para poder realizar los distintos servicios

    #ver solicitudes de servicios
    #aqui el profesional debe ver los servicios que se le han solicitado verificando disponibilidad anteriormente

    #ver servicios realizados
    #aqui se deben desplegar los servicios realizados por el profesional, si es una visita tecnica se debe agregar
    #el formulario guardado



]