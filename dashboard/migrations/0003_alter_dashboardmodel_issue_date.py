# Generated by Django 4.0.6 on 2022-07-31 21:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_dashboardmodel_issue_affect_other_areas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 31, 22, 19), null=True),
        ),
    ]