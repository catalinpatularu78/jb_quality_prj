# Generated by Django 4.0.5 on 2022-06-28 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_dashboardmodel_corrective_action_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardmodel',
            name='team_member',
        ),
    ]
