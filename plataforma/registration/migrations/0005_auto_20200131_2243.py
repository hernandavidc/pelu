# Generated by Django 3.0.2 on 2020-02-01 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_profile_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Cumpleaños'),
        ),
    ]