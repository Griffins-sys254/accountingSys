# Generated by Django 4.0.5 on 2022-07-12 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_ledger', '0011_auto_20220619_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitymanagementmodel',
            name='entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entity_permissions', to='django_ledger.entitymodel', verbose_name='Entity'),
        ),
        migrations.CreateModel(
            name='Mpesa_Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('transaction_mpesa_id', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
