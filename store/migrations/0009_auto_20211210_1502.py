# Generated by Django 3.2.8 on 2021-12-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_orderitem_flavor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flavor',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='flavor',
            field=models.ManyToManyField(null=True, to='store.Flavor'),
        ),
    ]
