from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from registration.models import Profile
from .models import Product, ProfitProduct
from .forms import ProductForm, ProfitProductForm

#Product Create lista los productos
class ProductListAndCreate(CreateView):
    template_name = 'products/productList.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:ListAndCreate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productList'] = self.request.user.profile.company.getProducts.all()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.company = request.user.profile.company
            product.save()
            return redirect(reverse_lazy('products:ListAndCreate') + '?register')
        return redirect(reverse_lazy('products:ListAndCreate') + '?error')

class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/productUpdateForm.html'
    success_url = reverse_lazy('products:ListAndCreate')

    def get(self, request, *args, **kwargs):
        if Product.objects.get(id=kwargs['pk']).company == self.request.user.profile.company:
            return super(UpdateView, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('products:ListAndCreate'))

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products:ListAndCreate')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if Product.objects.get(id=kwargs['pk']).company == request.user.profile.company:
            return self.delete(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('products:ListAndCreate') + '?error')
        

#ProfitProduct Create lista los beneficios de los colaboradores por producto
class ProfitProductListAndCreate(CreateView):
    template_name = 'products/profitproductList.html'
    model = ProfitProduct
    form_class = ProfitProductForm
    success_url = reverse_lazy('products:profitsListAndCreate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['idProduct'] = ""
        context['profitproductList'] = ProfitProduct.objects.filter(product__company=self.request.user.profile.company)
        if ('id' in self.request.GET) and (self.request.GET['id'] != ''):
            idProduct = int(self.request.GET['id'])
            if Product.objects.get(id=idProduct).company == self.request.user.profile.company:
                context['idProduct'] = idProduct
                context['profitproductList'] = ProfitProduct.objects.filter(product__id=idProduct)
        context['possibleProfileUsers'] = Profile.objects.filter(company= self.request.user.profile.company)
        context['possibleProducts'] = Product.objects.filter(company= self.request.user.profile.company)
        
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            profitProduct = form.save(commit=False)
            if profitProduct.product.company == request.user.profile.company:
                profitProduct.save()
                return redirect(reverse_lazy('products:profitsListAndCreate') + '?register')
            else:
                profitProduct.delete()
        return redirect(reverse_lazy('products:profitsListAndCreate') + '?error')

class ProfitProductUpdate(UpdateView):
    model = ProfitProduct
    form_class = ProfitProductForm
    template_name = 'products/profitProductUpdateForm.html'
    success_url = reverse_lazy('products:profitsListAndCreate')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['possibleProfileUsers'] = Profile.objects.filter(company= self.request.user.profile.company)
        context['possibleProducts'] = Product.objects.filter(company= self.request.user.profile.company)
        context['profit'] =  self.get_object()
        return context

    def get(self, request, *args, **kwargs):
        if ProfitProduct.objects.get(id=kwargs['pk']).product.company == self.request.user.profile.company:
            return super(UpdateView, self).get(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('products:profitsListAndCreate'))

class ProfitProductDelete(DeleteView):
    model = ProfitProduct
    success_url = reverse_lazy('products:profitsListAndCreate')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if ProfitProduct.objects.get(id=kwargs['pk']).product.company == request.user.profile.company:
            return self.delete(request, *args, **kwargs)
        else:
            return redirect(reverse_lazy('products:profitsListAndCreate') + '?error')