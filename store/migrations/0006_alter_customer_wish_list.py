# Generated by Django 3.2.8 on 2021-12-09 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_order_delevery_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='wish_list',
            field=models.ManyToManyField(to='store.Product'),
        ),
    ]