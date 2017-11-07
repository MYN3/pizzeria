from django.contrib import admin
from pizzeria.models import Ingrediente, IngredienteAdmin,Pizza,PizzaAdmin


# Register your models here.
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Pizza, PizzaAdmin)
