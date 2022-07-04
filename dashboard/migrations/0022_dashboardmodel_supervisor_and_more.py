# Generated by Django 4.0.5 on 2022-07-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_remove_areaofissue_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardmodel',
            name='supervisor',
            field=models.ManyToManyField(blank=True, to='dashboard.supervisorteam'),
        ),
        migrations.AlterField(
            model_name='dashboardmodel',
            name='issue_affect_other_areas',
            field=models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=5, null=True),
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
