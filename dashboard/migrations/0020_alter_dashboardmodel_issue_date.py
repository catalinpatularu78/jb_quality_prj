# Generated by Django 3.2.15 on 2022-08-08 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_auto_20220808_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 8, 15, 12), null=True),
        ),
    ]
