# Generated by Django 5.0 on 2023-12-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_customer_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
