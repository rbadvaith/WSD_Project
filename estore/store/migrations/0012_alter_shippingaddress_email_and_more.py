# Generated by Django 5.0 on 2023-12-14 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]