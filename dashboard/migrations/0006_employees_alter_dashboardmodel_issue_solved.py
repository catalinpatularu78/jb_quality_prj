# Generated by Django 4.0.5 on 2022-06-25 23:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_location_tag_dashboardmodel_ncr_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_solved',
            field=models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=5, null=True),
        ),
    ]
