from django.db import models
from django.urls import reverse
from django.db.models import CharField
import math
from uuid import uuid4



# Register dashboard models in dashboard/admin.py


# Create your models here.
class CustomDurationField(CharField):

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
   
        s = (f'{math.floor(days)} D {math.floor(hours)} H {math.floor(minutes)} M') 

        s = super(CustomDurationField,self).get_prep_value(s)
        return self.to_python(s)
	

class DashboardModel(models.Model):

    
    issue_solved_type = {
        ('yes', 'Yes'),
        ('no', 'No'),
    }
    
    id = models.UUIDField( 
        primary_key=True,
        default=uuid4,
        editable=False)

    # Fields displayed on dashboard page
    
    area = models.ManyToManyField('AreaOfIssue',blank=True)
    
    closure_date = models.DateField(null=True, blank = True)
    cost = models.FloatField(null=True ,blank = True)
    issue_date = models.DateField(null=True, blank = True)
    issue_solved = models.CharField(max_length = 5 , null=True, blank=True , choices= issue_solved_type)
    job_reference_number = models.CharField(max_length =100 , null=True ,blank = True)
    location = models.ManyToManyField('Locations' ,blank=True)
    ncr_number =  models.CharField(max_length =100 , null=True, blank = True )
    
    
    # additional fields displayed on create + detail + update 
    advice_number =  models.CharField(max_length =100 , null=True, blank = True )
    corrective_action = models.TextField(null=True , blank = True)
    description = models.TextField(null=True , blank = True)
    downtime_time = CustomDurationField (max_length =100, null=True)
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
        return str(self.id)
    
    
    def get_absolute_url(self):
        return reverse("record_detail", args=[str(self.id)])
    


    


class AreaOfIssue(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
    
class Locations(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
class Employees(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
    
class SupervisorTeam(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name
