# pylint: skip-file
# Generated by Django 3.2.8 on 2021-11-11 13:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('django_ledger', '0004_auto_20211005_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseordermodel',
            name='po_title',
            field=models.CharField(max_length=250, validators=[
                django.core.validators.MinLengthValidator(limit_value=5, message='PO Title must be greater than 5')],
                                   verbose_name='Purchase Order Title'),
        ),
    ]