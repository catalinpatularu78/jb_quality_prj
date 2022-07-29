# Generated by Django 4.0.6 on 2022-07-29 16:45

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaOfIssue',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerIssues',
            fields=[
                ('issue_area_name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Customer Issues',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='OtherIssues',
            fields=[
                ('issue_area_name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Other Issues',
            },
        ),
        migrations.CreateModel(
            name='ProductionIssues',
            fields=[
                ('issue_area_name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Production Issues',
            },
        ),
        migrations.CreateModel(
            name='SupervisorTeam',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierIssues',
            fields=[
                ('issue_area_name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Supplier Issues',
            },
        ),
        migrations.CreateModel(
            name='DashboardModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('client', models.CharField(blank=True, max_length=200, null=True)),
                ('closure_date', models.DateTimeField(blank=True, null=True)),
                ('cost', models.FloatField(blank=True, null=True)),
                ('issue_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 29, 17, 45), null=True)),
                ('issue_solved', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=5, null=True)),
                ('job_reference_number', models.CharField(blank=True, max_length=100, null=True)),
                ('ncr_number', models.CharField(blank=True, max_length=100, null=True)),
                ('advice_number', models.CharField(blank=True, max_length=100, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('corrective_action', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('downtime_time', models.IntegerField(blank=True, null=True)),
                ('estimated_completion_time', models.IntegerField(blank=True, null=True)),
                ('images', models.CharField(blank=True, max_length=300, null=True)),
                ('interim_containment_action', models.TextField(blank=True, null=True)),
                ('issue_affect_other_areas', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=5, null=True)),
                ('issue_affect_other_areas_description', models.TextField(blank=True, null=True)),
                ('ncr_creator', models.CharField(blank=True, max_length=200, null=True)),
                ('prevented_reoccurrence', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=5, null=True)),
                ('result_validation_action', models.TextField(blank=True, null=True)),
                ('root_cause', models.TextField(blank=True, null=True)),
                ('severity', models.PositiveIntegerField(blank=True, null=True)),
                ('area', models.ManyToManyField(blank=True, to='dashboard.areaofissue')),
                ('customer_issues', models.ManyToManyField(blank=True, to='dashboard.customerissues')),
                ('employee', models.ManyToManyField(blank=True, to='dashboard.employees')),
                ('location', models.ManyToManyField(blank=True, to='dashboard.locations')),
                ('other_issues', models.ManyToManyField(blank=True, to='dashboard.otherissues')),
                ('production_issue', models.ManyToManyField(blank=True, to='dashboard.productionissues')),
                ('supervisor', models.ManyToManyField(blank=True, to='dashboard.supervisorteam')),
                ('supplier_issue', models.ManyToManyField(blank=True, to='dashboard.supplierissues')),
            ],
        ),
    ]
