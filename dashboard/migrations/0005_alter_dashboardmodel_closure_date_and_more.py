# Generated by Django 4.1 on 2022-08-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_dashboardmodel_closure_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardmodel',
            name='closure_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='target_completion_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
