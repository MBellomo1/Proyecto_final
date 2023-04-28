from django.db import models

class animals(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()

class persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()