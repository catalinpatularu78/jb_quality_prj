# Generated by Django 4.1 on 2022-08-04 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_alter_dashboardmodel_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 4, 13, 26), null=True),
        ),
    ]