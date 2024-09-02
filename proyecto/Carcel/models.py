from django.db import models
from django.shortcuts import render

class Presos(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, unique=True)
    nacimiento = models.DateField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Agregar preso"
        verbose_name_plural = "Agregar presos"


class Policia(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Agregar preso"
        verbose_name_plural = "Agregar presos"

    

