# Generated by Django 4.1 on 2022-08-20 14:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
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
            name='DashboardModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('closure_date', models.DateTimeField(blank=True, null=True)),
                ('target_completion_date', models.DateTimeField(blank=True, null=True)),
                ('cost', models.FloatField(blank=True, null=True)),
                ('issue_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('store_issue_date', models.CharField(blank=True, max_length=100, null=True)),
                ('issue_solved', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=5, null=True)),
                ('job_reference_number', models.CharField(blank=True, max_length=100, null=True)),
                ('ncr_number', models.IntegerField(blank=True, null=True)),
                ('advice_number', models.CharField(blank=True, max_length=100, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('corrective_action', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('downtime_time', models.IntegerField(blank=True, null=True)),
                ('estimated_completion_time', models.IntegerField(blank=True, null=True)),
                ('interim_containment_action', models.TextField(blank=True, null=True)),
                ('issue_affect_other_areas', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=5, null=True)),
                ('issue_affect_other_areas_description', models.TextField(blank=True, null=True)),
                ('ncr_creator', models.CharField(blank=True, max_length=200, null=True)),
                ('prevented_reoccurrence', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], max_length=5, null=True)),
                ('result_validation_action', models.TextField(blank=True, null=True)),
                ('root_cause', models.TextField(blank=True, null=True)),
                ('severity', models.PositiveIntegerField(blank=True, null=True)),
                ('area', models.ManyToManyField(blank=True, to='dashboard.areaofissue')),
            ],
            options={
                'ordering': ['-ncr_number'],
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
                ('description', models.TextField(blank=True, default='')),
                ('PersonResponsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.personresponsible', verbose_name='Person/Company responsible')),
                ('company_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.clientmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='')),
                ('PersonResponsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.personresponsible', verbose_name='Person/Company responsible')),
                ('company_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.clientmodel')),
            ],
            options={
                'verbose_name_plural': 'Production Companies (Clients)',
            },
        ),
        migrations.CreateModel(
            name='OtherCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='')),
                ('PersonResponsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.personresponsible', verbose_name='Person/Company responsible')),
                ('company_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.clientmodel')),
            ],
            options={
                'verbose_name_plural': 'Other Companies (Clients)',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images', validators=[django.core.validators.validate_image_file_extension])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.dashboardmodel')),
            ],
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
                ('description', models.TextField(blank=True, default='')),
                ('PersonResponsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.personresponsible', verbose_name='Person/Company responsible')),
                ('company_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.clientmodel')),
            ],
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='area_in_specific',
            field=models.ManyToManyField(blank=True, to='dashboard.specificareaofissue'),
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='client',
            field=models.ManyToManyField(blank=True, to='dashboard.clientmodel'),
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='customer_issues',
            field=models.ManyToManyField(blank=True, to='dashboard.customerissues'),
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='location',
            field=models.ManyToManyField(blank=True, to='dashboard.locations'),
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='other_issues',
            field=models.ManyToManyField(blank=True, to='dashboard.otherissues'),
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='printed_by',
            field=models.ManyToManyField(blank=True, to='dashboard.qualityengineerteam'),
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='production_issue',
            field=models.ManyToManyField(blank=True, to='dashboard.productionissues'),
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='supervisor',
            field=models.ManyToManyField(blank=True, to='dashboard.supervisorteam'),
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='supplier_issue',
            field=models.ManyToManyField(blank=True, to='dashboard.supplierissues'),
        ),
        migrations.AddField(
            model_name='dashboardmodel',
            name='the_subject_responsible',
            field=models.ManyToManyField(blank=True, to='dashboard.personresponsible'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='')),
                ('PersonResponsible', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.personresponsible', verbose_name='Person/Company responsible')),
                ('company_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='dashboard.clientmodel')),
            ],
        ),
    ]
