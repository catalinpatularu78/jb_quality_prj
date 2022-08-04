# Generated by Django 4.1 on 2022-08-04 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_dashboardmodel_issue_date_supplier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 4, 15, 33), null=True),
        ),
        migrations.AlterField(
            model_name='deliverypartner',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='employee',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='othercompany',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='productioncompany',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
