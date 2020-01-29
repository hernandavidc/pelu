from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    RUT = models.CharField(max_length=100, null=True, blank=True)
    direction = models.CharField(verbose_name="Dirección", max_length=200, null=True, blank=True)
    contactNumber = models.CharField(verbose_name="Número de contacto", max_length=15, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return str(self.id)+" "+str(self.RUT)+" "+self.name

class Occupation(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name="Activo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return str(self.id)+" "+self.name
