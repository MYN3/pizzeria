from django.db import models
from django.contrib import admin


#Define la clase Actor, esta tabla no se relaciona con nadie más.

class Ingrediente(models.Model):
    nombre  =   models.CharField(max_length=30)
    cantidad = models.IntegerField()
    def __str__(self):
        return self.nombre
# Create your models here.

class Pizza(models.Model):
    nombre    = models.CharField(max_length=60)
    tamano     = models.IntegerField()
    ingredientes   = models.ManyToManyField(Ingrediente, through='Preparacion')
    def __str__(self):
        return self.nombre

class Preparacion (models.Model):
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

class PreparacionInLine(admin.TabularInline):
    model = Preparacion
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1

class IngredienteAdmin(admin.ModelAdmin):
    inlines = (PreparacionInLine,)

class PizzaAdmin (admin.ModelAdmin):
    inlines = (PreparacionInLine,)
