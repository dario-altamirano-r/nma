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

    #seccion calendario
    path('homeAdmin/verCalendario/', views.verCalendario, name = 'verCalendario'),

#-----------------------------------------------------------------------------------------#

    #vista de cliente
    #en el homeCliente, debe estar el estado general, cantidades de visitas, asesorias y capacitaciones
    #accesos a las demas secciones
    path('homeCliente/', views.homeCliente, name = 'homeCliente'),

    #detallePlan
    #aqui debe verse el detalle del plan con sus cantidades de visitas, asesorias y capacitaciones
    #ademas del monto actual del plan mas los servicios adicionales solicitados
    path('miPlan/', views.miPlan, name = 'miPlan'),

    #estadoCuenta
    #en este menu deben verse todo lo relacionado con los pagos, ya sea los realizados, los por pagar, etc
    #ademas de un detalle de los pagos realizados, por que medios, etc
    #en este menu tambien debe pagar!
    path('estadoCuenta/', views.estadoCuenta, name = 'estadoCuenta'),

    #servicios
    #en este menu debe desplegarse que tipo de servicio necesita, si es asesoria, capacitacion o visita
    #acordando disponibilidad de acuerdo a fecha y completar el formulario que corresponda segun el caso
    path('servicios/', views.servicios, name = 'servicios'),

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