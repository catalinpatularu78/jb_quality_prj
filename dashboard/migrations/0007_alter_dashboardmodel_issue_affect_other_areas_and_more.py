# Generated by Django 4.1 on 2022-08-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_dashboardmodel_closure_date_and_more'),
    ]

    operations = [
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
