# Generated by Django 4.2.3 on 2023-07-24 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_product_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vendor',
        ),
    ]