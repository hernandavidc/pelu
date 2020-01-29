from django.db import models

from django.contrib.auth.models import User
from companies.models import Company

class payment(models.Model):
    user = models.ForeignKey(User, verbose_name="Colaborador", related_name="getUserPayments", on_delete=models.PROTECT)
    paymentManager = models.ForeignKey(User, verbose_name="Responsable de pago", related_name="getManagerPayments", on_delete=models.PROTECT)
    company = models.ForeignKey(Company, verbose_name="Empresa", related_name="getCompanyPayments", on_delete=models.PROTECT)
    value = models.FloatField(verbose_name="Valor", null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return str(self.user)+ ' $' + str(self.value)
