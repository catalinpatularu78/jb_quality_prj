# Generated by Django 4.0.6 on 2022-07-30 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_alter_dashboardmodel_issue_affect_other_areas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 30, 13, 59), null=True),
        ),
    ]
