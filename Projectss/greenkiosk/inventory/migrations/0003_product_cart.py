# Generated by Django 4.2.3 on 2023-07-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('inventory', '0002_product_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cart',
            field=models.ManyToManyField(to='cart.cart'),
        ),
    ]