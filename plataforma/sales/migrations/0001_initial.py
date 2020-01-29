# Generated by Django 3.0.2 on 2020-01-29 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyerName', models.CharField(blank=True, max_length=200, null=True, verbose_name='Comprador')),
                ('buyerContact', models.CharField(blank=True, max_length=15, null=True, verbose_name='Número de contacto')),
                ('discount', models.FloatField(default=0, verbose_name='Descuento sobre la factura')),
                ('tax', models.FloatField(default=0, verbose_name='Impuesto')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='getSales', to='companies.Company', verbose_name='Empresa')),
                ('saleManager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='getSales', to=settings.AUTH_USER_MODEL, verbose_name='Responsable de venta')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='Cantidad')),
                ('costPerUnit', models.FloatField(verbose_name='Valor unitario')),
                ('discount', models.FloatField(default=0, verbose_name='Descuento sobre el producto')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_details_sale', to='products.Product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_details', to='sales.Sale')),
            ],
            options={
                'verbose_name': 'Detalle venta',
                'verbose_name_plural': 'Detalles venta',
            },
        ),
    ]
