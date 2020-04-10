from django import forms
from django.contrib.auth.models import User

from .models import Product, ProfitProduct

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'value','description']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre*', 'required': True}),
            'value': forms.NumberInput(attrs={'min':'0', 'class':'form-control', 'placeholder':'Valor*', 'required': True}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descipción'}),
        }

        labels = { #En el template <small>Los campos con * son requeridos</small>
            'name':'Nombre*',
            'value':'Valor*',
            'description':'Descripción',
        }

class ProfitProductForm(forms.ModelForm):
     #selects directamente en el documento html
    class Meta:
        model = ProfitProduct
        fields = ['user', 'product','profit']