# Generated by Django 4.2.2 on 2023-07-03 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contact_number', models.CharField(max_length=20)),
                ('delivery_date', models.DateField()),
                ('delivery_time', models.TimeField()),
                ('delivery_address', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=25)),
            ],
        ),
    ]
