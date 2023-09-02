# Generated by Django 4.1.5 on 2023-09-01 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_alter_apartmentattributes_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentattributes',
            name='property',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apartment_attributes', to='properties.property', verbose_name='Apartment attributes'),
        ),
    ]
