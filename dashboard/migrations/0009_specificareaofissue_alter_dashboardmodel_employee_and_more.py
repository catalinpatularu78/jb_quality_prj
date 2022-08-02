# Generated by Django 4.0.6 on 2022-08-01 20:27

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_dashboardmodel_area_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecificAreaOfIssue',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='employee',
            field=models.ManyToManyField(blank=True, to='dashboard.employees'),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 1, 21, 27), null=True),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='location',
            field=models.ManyToManyField(blank=True, to='dashboard.locations'),
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='area_in_specific',
            field=models.ManyToManyField(blank=True, to='dashboard.specificareaofissue'),
        ),
    ]