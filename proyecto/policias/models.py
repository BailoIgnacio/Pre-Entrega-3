from django.db import models

class Policia(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Agregar policia"
        verbose_name_plural = "Agregar policias"



    