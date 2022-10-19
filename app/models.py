from django.db import models
import datetime

# Create your models here.

#Tabla Administrador
class Administrador(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    email = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)

#Tabla Cliente
class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombreEmpresa = models.CharField(max_length=255, default="")
    email = models.CharField(max_length=255)
    rubro = models.CharField(max_length=255, default="")
    tamanio = models.IntegerField(default=0)
    mutualidad = models.CharField(max_length=255, default="")
    numeroTelefono = models.CharField(max_length=20, default="")
    contrasena = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.rut+" - "+self.email+" - "+self.contrasena 


#Tabla Plan
class Plan(models.Model):
    id = models.AutoField(primary_key=True)
    rutCliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=False)
    montoPlan = models.IntegerField(default=0)
    cantidadVisitas = models.IntegerField(default=0)
    cantidadAsesorias = models.IntegerField(default=0)
    cantidadCapacitaciones = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)+" - "+str(self.rutCliente.rut)+" - "+int(self.montoPlan)+" - "+int(self.cantidadVisitas)+" - "+int(self.cantidadAsesorias)+" - "+int(self.cantidadCapacitaciones)


#Tabla Pago
class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    rutCliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=False)
    montoPagado = models.IntegerField()

    def __str__(self):
        return self.id+" - "+str(self.rutCliente.rut)+" - "+int(self.montoPagado) 


#Tabla Profesional
class Profesional(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombreCompleto = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255,default="")
    contrasena = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.rut+" - "+self.nombreCompleto+" - "+self.email+" - "+self.contrasena 


#Tabla Asesoria
class Asesoria(models.Model):
    id = models.AutoField(primary_key=True)
    rutCliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=False)
    rutProfesional = models.ForeignKey(Profesional, models.DO_NOTHING, blank=False)
    motivo = models.CharField(max_length=255)

    def __str__(self):
        return self.id+" - "+str(self.rutCliente.rut)+" - "+str(self.rutProfesional.rut)+" - "+self.motivo


#Tabla Capacitacion
class Capacitacion(models.Model):
    id = models.AutoField(primary_key=True)
    rutCliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=False)
    rutProfesional = models.ForeignKey(Profesional, models.DO_NOTHING, blank=False)
    fecha = models.CharField(default=datetime.date.today().strftime('%d/%m/%Y'), max_length=10)
    cantidadAsistentes = models.IntegerField()
    motivo = models.CharField(max_length=255)

    def __str__(self):
        return self.id+" - "+str(self.rutCliente.rut)+" - "+str(self.rutProfesional.rut)+" - "+self.fecha+" - "+self.motivo


#Tabla Visita
class Visita(models.Model):
    id = models.AutoField(primary_key=True)
    rutCliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=False)
    rutProfesional = models.ForeignKey(Profesional, models.DO_NOTHING, blank=False)
    fecha = models.CharField(default=datetime.date.today().strftime('%d/%m/%Y'), max_length=10)
    observaciones = models.CharField(max_length=255)
    recomendaciones = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.id+" - "+str(self.rutCliente.rut)+" - "+str(self.rutProfesional.rut)+" - "+self.fecha+" - "+self.observaciones


#Tabla Chequeo
class Chequeo(models.Model):
    id = models.AutoField(primary_key=True)
    idVisita = models.ForeignKey(Visita, models.DO_NOTHING, blank=False)
    rutCliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=False)
    rutProfesional = models.ForeignKey(Profesional, models.DO_NOTHING, blank=False)

    def __str__(self):
        return self.id+" - "+str(self.rutCliente.rut)+" - "+str(self.rutProfesional.rut)+" - "+self.fecha+" - "+self.motivo


