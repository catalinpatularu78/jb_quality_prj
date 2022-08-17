# Generated by Django 4.1 on 2022-08-16 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_dashboardmodel_issue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_affect_other_areas',
            field=models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 16, 21, 41), null=True),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_solved',
            field=models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='prevented_reoccurrence',
            field=models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=5, null=True),
        ),
    ]
