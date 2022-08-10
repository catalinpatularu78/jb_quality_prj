# Generated by Django 4.1 on 2022-08-10 21:00

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
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
            name='ClientModel',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Clients',
                'ordering': ['name'],
            },
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
            name='PersonResponsible',
            fields=[
                ('title', models.CharField(default='', max_length=255)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Person/Company Responsible',
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
            name='QualityEngineerTeam',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecificAreaOfIssue',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
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
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('PersonResponsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.personresponsible', verbose_name='Person/Company responsible')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('PersonResponsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.personresponsible', verbose_name='Person/Company responsible')),
            ],
            options={
                'verbose_name_plural': 'Production Companies (Clients)',
            },
        ),
        migrations.CreateModel(
            name='OtherCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('PersonResponsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.personresponsible', verbose_name='Person/Company responsible')),
            ],
            options={
                'verbose_name_plural': 'Other Companies (Clients)',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.CharField(default='', max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.personresponsible')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('PersonResponsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.personresponsible', verbose_name='Person/Company responsible')),
            ],
        ),
        migrations.CreateModel(
            name='DashboardModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('closure_date', models.DateTimeField(blank=True, null=True)),
                ('target_completion_date', models.DateTimeField(blank=True, null=True)),
                ('cost', models.FloatField(blank=True, null=True)),
                ('issue_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 10, 22, 0), null=True)),
                ('issue_solved', models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=5, null=True)),
                ('job_reference_number', models.CharField(blank=True, max_length=100, null=True)),
                ('ncr_number', models.CharField(blank=True, max_length=100, null=True)),
                ('advice_number', models.CharField(blank=True, max_length=100, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('corrective_action', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('downtime_time', models.IntegerField(blank=True, null=True)),
                ('estimated_completion_time', models.IntegerField(blank=True, null=True)),
                ('interim_containment_action', models.TextField(blank=True, null=True)),
                ('issue_affect_other_areas', models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=5, null=True)),
                ('issue_affect_other_areas_description', models.TextField(blank=True, null=True)),
                ('ncr_creator', models.CharField(blank=True, max_length=200, null=True)),
                ('prevented_reoccurrence', models.CharField(blank=True, choices=[('no', 'No'), ('yes', 'Yes')], max_length=5, null=True)),
                ('result_validation_action', models.TextField(blank=True, null=True)),
                ('root_cause', models.TextField(blank=True, null=True)),
                ('severity', models.PositiveIntegerField(blank=True, null=True)),
                ('image_upload', models.ImageField(blank=True, null=True, upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg'])])),
                ('area', models.ManyToManyField(blank=True, to='dashboard.areaofissue')),
                ('area_in_specific', models.ManyToManyField(blank=True, to='dashboard.specificareaofissue')),
                ('client', models.ManyToManyField(blank=True, to='dashboard.clientmodel')),
                ('customer_issues', models.ManyToManyField(blank=True, to='dashboard.customerissues')),
                ('location', models.ManyToManyField(blank=True, to='dashboard.locations')),
                ('other_issues', models.ManyToManyField(blank=True, to='dashboard.otherissues')),
                ('printed_by', models.ManyToManyField(blank=True, to='dashboard.qualityengineerteam')),
                ('production_issue', models.ManyToManyField(blank=True, to='dashboard.productionissues')),
                ('supervisor', models.ManyToManyField(blank=True, to='dashboard.supervisorteam')),
                ('supplier_issue', models.ManyToManyField(blank=True, to='dashboard.supplierissues')),
                ('the_subject_responsible', models.ManyToManyField(blank=True, to='dashboard.personresponsible')),
            ],
            options={
                'ordering': ['-issue_date'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('PersonResponsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.personresponsible', verbose_name='Person/Company responsible')),
            ],
        ),
    ]
