from django.db import models
<<<<<<< HEAD
from django.urls import reverse
from datetime import datetime

from uuid import uuid4



# Register dashboard models in dashboard/admin.py

# Create your models here.
=======
from django.db.models import IntegerField
from django.urls import reverse
from django.db.models import CharField
import math
from uuid import uuid4
from django.utils import formats
from django.core.exceptions import ValidationError

# Register dashboard models in dashboard/admin.py


# Create your models here.
class CustomDuration(CharField):

    def to_python(self, value):

        duration = super().to_python(value)
        return str(duration)

    def get_prep_value(self, value):

        total_minutes = int(value)

        days = total_minutes // 1440
        daysInMinutes = days * 1440     
        hours = (total_minutes - daysInMinutes) // 60
        hoursInMinutes = hours * 60
        minutes = total_minutes - (daysInMinutes + hoursInMinutes)

        str = "{:02d}{:02d}{:02d}".format(days, hours, minutes)

        str = super(CustomDuration,self).get_prep_value(str)
        return self.to_python(str)



>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
class DashboardModel(models.Model):

    
    issue_solved_type = {
        ('yes', 'Yes'),
        ('no', 'No'),
    }
    
    id = models.UUIDField( 
        primary_key=True,
        default=uuid4,
<<<<<<< HEAD
        editable=False,
        max_length=36,)
=======
        editable=False)
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3

    # Fields displayed on dashboard page
    
    area = models.ManyToManyField('AreaOfIssue',blank=True)
<<<<<<< HEAD
    client = models.CharField(max_length =200 , null=True, blank = True )
    closure_date = models.DateTimeField(null=True, blank = True)
    cost = models.FloatField(null=True ,blank = True)
    issue_date = models.DateTimeField(null=True, blank = True , default = datetime.now().replace(second=0, microsecond=0) )#default = timezone.localtime
=======
    
    closure_date = models.DateField(null=True, blank = True)
    cost = models.FloatField(null=True ,blank = True)
    issue_date = models.DateField(null=True, blank = True)
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
    issue_solved = models.CharField(max_length = 5 , null=True, blank=True , choices= issue_solved_type)
    job_reference_number = models.CharField(max_length =100 , null=True ,blank = True)
    location = models.ManyToManyField('Locations' ,blank=True)
    ncr_number =  models.CharField(max_length =100 , null=True, blank = True )
    
    
    # additional fields displayed on create + detail + update 
    advice_number =  models.CharField(max_length =100 , null=True, blank = True )
<<<<<<< HEAD
    comments = models.TextField(null=True , blank = True)
    corrective_action = models.TextField(null=True , blank = True)
    description = models.TextField(null=True , blank = True)
    downtime_time = models.IntegerField (null=True, blank = True)
    employee = models.ManyToManyField('Employees' ,blank=True)
    estimated_completion_time = models.IntegerField (null=True, blank = True)
    images = models.CharField(max_length =300 , null=True, blank = True)
    interim_containment_action = models.TextField(null=True , blank = True)
    issue_affect_other_areas = models.CharField(max_length = 5 , null=True, blank=True , choices= issue_solved_type)
    issue_affect_other_areas_description = models.TextField(null=True , blank = True)
    ncr_creator = models.CharField(max_length =200 , null=True, blank = True )
    prevented_reoccurrence = models.CharField(max_length = 5 , null=True, blank=True , choices= issue_solved_type)
    result_validation_action = models.TextField(null=True , blank = True)
    root_cause = models.TextField(null=True , blank = True)
    severity = models.PositiveIntegerField(
        null=True,
        blank = True,
    )
    supervisor = models.ManyToManyField('SupervisorTeam' ,blank=True)
    
    # Quality issues area's 
    
    production_issue = models.ManyToManyField('ProductionIssues' ,blank=True)
    supplier_issue = models.ManyToManyField('SupplierIssues' ,blank=True)
    customer_issues = models.ManyToManyField('CustomerIssues' ,blank=True)
    other_issues = models.ManyToManyField('OtherIssues' ,blank=True)
    

    
    def __str__(self) -> str:
        if self.advice_number:return self.advice_number
=======
    corrective_action = models.TextField(null=True , blank = True)
    description = models.TextField(null=True , blank = True)
    downtime_time = CustomDuration(max_length =100)
    employee = models.ManyToManyField('Employees' ,blank=True)
    estimated_completion_time = models.IntegerField (null=True, blank = True)
    images = models.CharField(max_length =300 , null=True, blank = True) # hyperlink
    interim_containment_action = models.TextField(null=True , blank = True)
    issue_affect_other_areas = models.CharField(max_length = 5 , null=True, blank=True , choices= issue_solved_type)
    issue_affect_other_areas_description = models.TextField(null=True , blank = True)
    ncr_hyperlink = models.CharField(max_length =300 , null=True, blank = True)
    prevented_reoccurrence = models.CharField(max_length = 5 , null=True, blank=True , choices= issue_solved_type)
    result_validation_action = models.TextField(null=True , blank = True)
    root_cause = models.TextField(null=True , blank = True)
    supervisor = models.ManyToManyField('SupervisorTeam' ,blank=True)
    
    


    
    
    
    
    
    
    
    
    def __str__(self) -> str:
        if self.job_reference_number:
            return self.job_reference_number
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
        return str(self.id)
    
    
    def get_absolute_url(self):
        return reverse("record_detail", args=[str(self.id)])
    
<<<<<<< HEAD
    
    def time_format_converter(self, minutes):
        if minutes == None : return "" 
        return ( f'{minutes // 1440} days , {((minutes // 60) % 24)} hours , {minutes % 60} minutes')
    
    
    @property
    def downtime_readability(self):
        readable_downtime = self.downtime_time
        formatted_readable_date_str = self.time_format_converter(readable_downtime)
        return (formatted_readable_date_str)
    
    @property
    def estimated_readability(self):
        readable_estimated = self.estimated_completion_time
        formatted_est_date_str = self.time_format_converter(readable_estimated)
        return (formatted_est_date_str)
=======
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3


    


class AreaOfIssue(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)
<<<<<<< HEAD
    
    def __str__(self):
        return self.name


class ProductionIssues(models.Model):
    issue_area_name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.issue_area_name
    

    class Meta:
        verbose_name_plural = "Production Issues"
    

    
class SupplierIssues(models.Model):
    issue_area_name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.issue_area_name
    
    class Meta:
        verbose_name_plural = "Supplier Issues"    
    
class CustomerIssues(models.Model):
    issue_area_name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.issue_area_name

    class Meta:
        verbose_name_plural = "Customer Issues"
        
class OtherIssues(models.Model):
    issue_area_name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.issue_area_name
    
    class Meta:
        verbose_name_plural = "Other Issues"
=======

    def __str__(self):
        return self.name
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
    
    
class Locations(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
<<<<<<< HEAD
    class Meta:
        verbose_name_plural = "Locations"
    
=======
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
class Employees(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
<<<<<<< HEAD
    class Meta:
        verbose_name_plural = "Employees"
    
=======
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
    
class SupervisorTeam(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name
<<<<<<< HEAD


=======
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
