from django.db import models
from django.db.models.fields import CharField
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Marca(models.Model):
    descripcion = models.CharField(max_length=500)

    fechaActualizacion = models.DateTimeField( default = datetime.now)
    actualizadoPor = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.descripcion

class MarcaProcesador(models.Model):
    descripcion = models.CharField(max_length=200)
    
    fechaActualizacion = models.DateTimeField(default = datetime.now)
    actualizadoPor = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.descripcion

class Ram(models.Model):
    descripcion = models.CharField(max_length=500)
    velocidad = models.FloatField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    fechaActualizacion = models.DateTimeField(default = datetime.now)
    actualizadoPor = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.descripcion

class Disco(models.Model):
    descripcion= models.CharField(max_length=250)
    tipo = models.CharField(max_length=250) # SSD, HardDisk, M2 SSD
    velocidad = models.FloatField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    fechaActualizacion = models.DateTimeField(default = datetime.now)
    actualizadoPor = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.descripcion

class Procesador(models.Model):
    descripcion = models.CharField(max_length=250)
    marcaProcesador = models.ForeignKey(MarcaProcesador, default= 1,on_delete=models.CASCADE)
    velocidad = models.FloatField()
    generacion = models.IntegerField(default=0)

    fechaActualizacion = models.DateTimeField(default = datetime.now)
    actualizadoPor = models.ForeignKey(User, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.descripcion

class Computadora(models.Model ):
    descripcion = models.CharField(max_length=500)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE)
    retroiluminado = models.BooleanField(default=False)
    color = models.CharField(max_length=250)
    material = models.CharField(max_length=250) # plastico, metal, etc.
    lectorDeHuella = models.BooleanField(default=False)
    procesador = models.ForeignKey(Procesador, on_delete=models.CASCADE)
    duracionBateria = models.IntegerField(verbose_name='Duracion Bateria en Horas', default=0)
    #                                              ↑
    #                             cambiar el nombre de la columna en el panel de administraciion

    fechaActualizacion = models.DateTimeField(default = datetime.now)
    actualizadoPor = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    
    


    def __str__(self):
        return self.descripcion


