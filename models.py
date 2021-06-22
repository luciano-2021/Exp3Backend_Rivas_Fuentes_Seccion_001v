from django.db import models

# Create your models here.

class Tiporeceta(models.Model):
    idtipo = models.IntegerField(primary_key=True, verbose_name='id tipo receta')
    descripcion = models.CharField(max_length=20, verbose_name='descripcion')

    def __str__(self):
        return self.descripcion

class Recetas(models.Model):
    idrecetas = models.IntegerField(primary_key=True, verbose_name='Id recetas')
    nombrereceta = models.CharField(max_length=50, verbose_name='Nombre receta')
    descripcionreceta = models.CharField(max_length=150, verbose_name='Descripcion receta')
    tiporeceta = models.ForeignKey('tiporeceta', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombrereceta


