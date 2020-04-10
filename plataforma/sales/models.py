from django.db import models

from django.contrib.auth.models import User
from companies.models import Company
from products.models import Product

class Sale(models.Model):
    saleManager = models.ForeignKey(User, verbose_name="Responsable de venta", related_name="getSales", on_delete=models.PROTECT)
    company = models.ForeignKey(Company, verbose_name="Empresa", related_name="getSales", on_delete=models.PROTECT)
    buyerName = models.CharField(verbose_name="Comprador", max_length=200, null=True, blank=True)
    buyerContact = models.CharField(verbose_name="Número de contacto", max_length=15, null=True, blank=True)
    discount = models.FloatField(verbose_name="Descuento sobre la factura", default=0)
    tax = models.FloatField(verbose_name="Impuesto", default=0)
    total = models.FloatField(verbose_name="Total", default=0, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return str(self.id)+" "+str(self.saleManager)

class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, related_name="get_details", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="get_details_sale", on_delete=models.PROTECT)
    amount = models.FloatField(verbose_name="Cantidad", null=False, blank=False)
    costPerUnit = models.FloatField(verbose_name="Valor unitario", null=False, blank=False)
    discount = models.FloatField(verbose_name="Descuento sobre el producto", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Detalle venta"
        verbose_name_plural = "Detalles venta"

    def __str__(self):
        return self.product.name+", Cantidad: "+str(self.amount)+", Costo unidad: "+str(self.costPerUnit)
