# Generated by Django 4.0.6 on 2022-08-01 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_alter_dashboardmodel_issue_affect_other_areas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardmodel',
            name='target_completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_affect_other_areas',
            field=models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 1, 22, 3), null=True),
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
