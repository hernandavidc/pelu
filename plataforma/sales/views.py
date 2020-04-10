from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Sale, SaleDetail
from products.models import Product
from .forms import SaleForm, SaleDetailFormSet

#Product Create lista los productos
class SaleListAndCreate(CreateView):
    template_name = 'sales/saleList.html'
    model = Sale
    form_class = SaleForm
    success_url = reverse_lazy('sales:ListAndCreate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['saleList'] = self.request.user.profile.company.getSales.all()
        context['profictsProductList'] = self.request.user.getUserProficts.all()
        return context

    def get(self, request, *args, **kwargs):
        self.object = Sale()
        form = self.get_form(self.form_class)
        sale_detail_form_set=SaleDetailFormSet()
        return self.render_to_response(self.get_context_data(form=form,sale_detail_form_set=sale_detail_form_set))

    def post(self, request, *args, **kwargs):
        self.object = Sale()
        print(request.POST)
        form = self.get_form(self.form_class)
        sale_detail_form_set = SaleDetailFormSet(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.saleManager = request.user
            sale.company = request.user.profile.company
            sale.save()
            total = 0
            for item in range(int(request.POST['get_details-TOTAL_FORMS'])):
                detail = str(item)
                if not (request.POST.get('get_details-'+detail+'-DELETE', False) and request.POST['get_details-'+detail+'-DELETE'] == 'on'):
                    idProduct = int(request.POST['get_details-'+detail+'-product'])
                    amount = float(request.POST['get_details-'+detail+'-amount'])
                    discount = float(request.POST['get_details-'+detail+'-discount'])
                    product = Product.objects.get(pk=idProduct)
                    saleDetail = SaleDetail.objects.create(
                        sale = sale,
                        product = product,
                        amount = amount,
                        costPerUnit = product.value,
                        discount = discount
                    )
                    saleDetail.save()
                    total += product.value - (product.value * (discount/100))
            sale.total = total
            return redirect(self.success_url)
        else:
            return self.form_invalid(form, sale_detail_form_set)

    def form_valid(self, form, sale_detail_form_set):
        form = form.save()
        sale_detail_form_set.instance = form
        sale_detail_form_set.save()
        #Redireccionamos a la ventana del listado de compras
        return redirect(self.success_url)

    def form_invalid(self, form, sale_detail_form_set):
        return self.render_to_response(self.get_context_data(form=form,sale_detail_form_set = sale_detail_form_set))
