from pyexpat import model
from django.forms import *
from core.erp.models import Category

class CategoryForm(ModelForm):
    #sobreescribir el formulario 
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            # adicionar opciones que se pueden duplicar
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        #cambiar a todos los componentes
        self.fields['name'].widget.attrs['autofocus'] = True
    class Meta:
        model = Category
        fields = '__all__'
        #''' realizar excluciones  exclude = [campos]'''
        #Cambiar la propiedad de los componentes
        widgets = {
            # Colocar las clases adicionales
            'name': TextInput(
                attrs={
                  'placeholder':'Ingrese categoria',
                }

            ),
            'description': Textarea(
                attrs={
                    'placeholder':'Ingrese descripción',
                    'rows' :'3',
                    'cols': '3',
                }

            ),

        }

