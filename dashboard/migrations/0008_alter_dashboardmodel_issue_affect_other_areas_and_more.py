# Generated by Django 4.0.5 on 2022-07-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_remove_dashboardmodel_ncr_hyperlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_affect_other_areas',
            field=models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_date',
            field=models.DateField(blank=True, null=True),
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