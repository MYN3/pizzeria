

from django.shortcuts import render, get_object_or_404,redirect
#librería para manejar el envío de mensajes
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import PizzaForm, IngredienteForm
from pizzeria.models import Pizza, Preparacion, Ingrediente
from django.contrib.auth.decorators import login_required

def pizza_nueva(request):

    if request.method == "POST":

        formulario = PizzaForm(request.POST)


        if formulario.is_valid():

            pizza = Pizza.objects.create(nombre=formulario.cleaned_data['nombre'], tamano = formulario.cleaned_data['tamano'])

            for ingrediente_id in request.POST.getlist('ingredientes'):

                preparacion = Preparacion(ingrediente_id=ingrediente_id, pizza_id = pizza.id)

                preparacion.save()

            messages.add_message(request, messages.SUCCESS, 'Pizza Guardada Exitosamente')

    else:

        formulario = PizzaForm()

    return render(request, 'pizzeria/pizza_nueva.html', {'formulario': formulario})

def pizza_lista(request):
    pizzas = Pizza.objects.all()
    return render(request, 'pizzeria/pizza_lista.html', {'pizzas':pizzas})

@login_required
def ingrediente_lista(request):
    ingrediente = Ingrediente.objects.all()
    return render(request, 'pizzeria/ingrediente_lista.html', {'ingrediente':ingrediente})

def pizza_detail(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    return render(request, 'pizzeria/pizza_detail.html', {'pizza': pizza})

def pizza_remove(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    pizza.delete()
    return redirect('pizza_lista')

def pizza_editar(request, pk):
    pizza = get_object_or_404(Pizza, pk=pk)
    if request.method == "POST":
        formulario = PizzaForm(request.POST, instance=pizza)
        if formulario.is_valid():
            pizza = formulario.save(commit=False)
            pizza.save()
        return redirect('pizza_lista')
    else:
        formulario = PizzaForm(instance=pizza)
    return render(request, 'pizzeria/pizza_editar.html', {'formulario': formulario})

@login_required
def ingrediente_nuevo(request):
    if request.method == "POST":
        formulario = IngredienteForm(request.POST)
        if formulario.is_valid():
            ingrediente = formulario.save(commit=False)
            ingrediente = Ingrediente(nombre= formulario.cleaned_data['nombre'], cantidad = formulario.cleaned_data['cantidad'])
            ingrediente.save()
        messages.add_message(request, messages.SUCCESS, 'INgrediente Guardada Exitosamente')
    else:
        formulario = IngredienteForm()
    return render(request, 'pizzeria/ingrediente_nuevo.html', {'formulario': formulario})
