from django.db import models

from django.contrib.auth.models import User
from companies.models import Company

class Product(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200, null=False, blank=False)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name="getProducts")
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    value = models.FloatField(verbose_name="Valor", null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name

class ProfitProduct(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="getUserProficts")
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="getProductProficts")
    profit = models.FloatField(verbose_name="Valor", null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Beneficio por producto"
        verbose_name_plural = "Beneficios por producto"

    def __str__(self):
        return str(self.name.user) + ' ' + self.product.name + ' ' + self.profit

