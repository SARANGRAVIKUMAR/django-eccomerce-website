# Generated by Django 3.0.6 on 2020-05-14 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='quantity_price',
        ),
    ]
