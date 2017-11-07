from django import forms

from .models import Pizza, Ingrediente


class PizzaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Pizza
        fields = ('nombre', 'tamano', 'ingredientes')

#Redefinimos que control (widget) vamos a mostrar para ingresar los actores.

#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.


        def __init__ (self, *args, **kwargs):
            super(PizzaForm, self).__init__(*args, **kwargs)
            self.fields["ingredientes"].widget = forms.widgets.CheckboxSelectMultiple()
            self.fields["ingredientes"].help_text = "Ingrese los Ingredientes que llevara la Pizza"
            self.fields["ingredientes"].queryset = Ingrediente.objects.all()


class IngredienteForm(forms.ModelForm):

    class Meta:
        model = Ingrediente
        fields = ('nombre', 'cantidad')
