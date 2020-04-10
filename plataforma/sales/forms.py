from django import forms
from django.forms.models import inlineformset_factory

from products.models import Product
from .models import Sale, SaleDetail

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['buyerName', 'buyerContact','discount','tax','total']

    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class SaleDetailForm(forms.ModelForm):
    class Meta:
        model = SaleDetail
        fields = ['product','amount','costPerUnit','discount']

    def __init__(self, *args, **kwargs):
        super(SaleDetailForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount == '':
            raise forms.ValidationError("Debe ingresar una cantidad valida")
        return amount

    def clean_costPerUnit(self):
        costPerUnit = self.cleaned_data['costPerUnit']
        if costPerUnit == '':
            raise forms.ValidationError("Debe ingresar un precio valido")

SaleDetailFormSet = inlineformset_factory(Sale, SaleDetail, form=SaleDetailForm, extra=0)