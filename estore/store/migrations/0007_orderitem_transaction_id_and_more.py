# Generated by Django 5.0 on 2023-12-13 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_shippingaddress_email_shippingaddress_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
