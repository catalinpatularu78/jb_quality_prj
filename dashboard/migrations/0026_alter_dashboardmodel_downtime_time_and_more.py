# Generated by Django 4.0.5 on 2022-07-06 12:12

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_alter_dashboardmodel_issue_affect_other_areas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardmodel',
            name='downtime_time',
            field=dashboard.models.CustomDurationField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_affect_other_areas',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_solved',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='prevented_reoccurrence',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=5, null=True),
        ),
    ]
