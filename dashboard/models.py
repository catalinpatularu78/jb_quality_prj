from django.db import models
from django.urls import reverse
from datetime import datetime
from uuid import uuid4
from django.conf import settings
from django.core import validators
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class DashboardModel(models.Model):


    
    issue_solved_type = {
        ('yes', 'Yes'),
        ('no', 'No'),
    }
    
    id = models.UUIDField( 
        primary_key=True,
        default=uuid4,
        editable=False,
        max_length=36,)


    # Fields displayed on dashboard page

    area = models.ManyToManyField('AreaOfIssue',blank=True)
    client = models.ManyToManyField('ClientModel' ,blank=True)
    closure_date = models.DateTimeField(null=True, blank = True)
    target_completion_date = models.DateTimeField(null=True, blank = True)
    cost = models.FloatField(null=True ,blank = True)
    issue_date = models.DateTimeField(null=True, blank = True , default = datetime.now().replace(second=0, microsecond=0) )#default = timezone.localtime
    issue_solved = models.CharField(max_length = 5 , null=True, blank=True , choices= issue_solved_type)
    job_reference_number = models.CharField(max_length =100 , null=True ,blank = True)
    location = models.ManyToManyField('Locations' ,blank=True)
    ncr_number =  models.CharField(max_length =100 , null=True)
    # ncr_number =  models.IntegerField( default=0 , unique=True, blank=True, null=True)
    
    
    # additional fields displayed on create + detail + update 
    advice_number =  models.CharField(max_length =100 , null=True, blank = True)
    comments = models.TextField(null=True , blank = True)
    corrective_action = models.TextField(null=True , blank = True)
    description = models.TextField(null=True , blank = True, default="")
    downtime_time = models.IntegerField (null=True, blank = True)
    the_subject_responsible = models.ManyToManyField('PersonResponsible' ,blank=True) #changed name here, and aOK
    estimated_completion_time = models.IntegerField (null=True, blank = True)
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
    image_upload = models.ImageField(upload_to="images/", null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])
    supervisor = models.ManyToManyField('SupervisorTeam' ,blank=True)
    printed_by = models.ManyToManyField('QualityEngineerTeam', blank=True) 
    
    # Quality issues area's 
    production_issue = models.ManyToManyField('ProductionIssues' ,blank=True)
    supplier_issue = models.ManyToManyField('SupplierIssues' ,blank=True)
    customer_issues = models.ManyToManyField('CustomerIssues' ,blank=True)
    other_issues = models.ManyToManyField('OtherIssues' ,blank=True)

    #new
    area_in_specific = models.ManyToManyField('SpecificAreaOfIssue', blank=True)
    
    # ORDER DASHBOARD BY DATE  
    class Meta:
        ordering = ['-issue_date']
        
        
    def __str__(self) -> str:
        if self.ncr_number:return str(self.ncr_number)
        return str(self.id)
    
    
    def get_absolute_url(self):
        return reverse("record_detail", args=[str(self.id)])
    
    
    def time_format_converter(self, minutes):
        if minutes == None : return "" 
        return ( f'{minutes // 1440}d : {((minutes // 60) % 24)}h : {minutes % 60}m')
    

    
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


    

class SpecificAreaOfIssue(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)
    
    def __str__(self):
        return self.name


class AreaOfIssue(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)
    
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
    
    
class Locations(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Locations"
    

class SupervisorTeam(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name

class QualityEngineerTeam(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name


class PersonResponsible(models.Model):

    class Meta:
        verbose_name_plural = 'Person/Company Responsible'
  
  
    title = models.CharField(max_length=255, default='')
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.title


# added 10/08 might not be required - Conor to decide 
class ClientModel(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Clients'

''' 
ManyToOne Relationships 

These models will store data in the admin.
They won't be taking data on the dashboard_create page.
 '''

class Employee(models.Model):

    employee_number = models.CharField(max_length=255, default='')
    description = models.TextField(default='', blank=True)
    name = models.ForeignKey(PersonResponsible, null=True, on_delete=models.PROTECT) 

    def __str__(self):
        return self.employee_number


class Customer(models.Model):

    company_name = models.CharField(max_length=255, default='')
    description = models.TextField(default='', blank=True)
    PersonResponsible = models.ForeignKey(PersonResponsible, null=True, on_delete=models.PROTECT, verbose_name="Person/Company responsible") 
    
    def __str__(self):
        return self.company_name


class Supplier(models.Model):

    company_name = models.CharField(max_length=255, default='')
    description = models.TextField(default='', blank=True)
    PersonResponsible = models.ForeignKey(PersonResponsible, null=True, on_delete=models.PROTECT, verbose_name="Person/Company responsible") 
    
    def __str__(self):
        return self.company_name


class ProductionCompany(models.Model):
    
    class Meta:
        verbose_name_plural = 'Production Companies (Clients)'


    company_name = models.CharField(max_length=255, default='')
    description = models.TextField(default='', blank=True)
    PersonResponsible = models.ForeignKey(PersonResponsible, null=True, on_delete=models.PROTECT, verbose_name="Person/Company responsible")  
    
    def __str__(self):
        return self.company_name


class DeliveryPartner(models.Model):

    company_name = models.CharField(max_length=255, default='')
    description = models.TextField(default='', blank=True)
    PersonResponsible = models.ForeignKey(PersonResponsible, null=True, on_delete=models.PROTECT, verbose_name="Person/Company responsible")  
    
    def __str__(self):
        return self.company_name


class OtherCompany(models.Model):

    class Meta:
        verbose_name_plural = 'Other Companies (Clients)'

    company_name = models.CharField(max_length=255, default='')
    description = models.TextField(default='', blank=True)
    PersonResponsible = models.ForeignKey(PersonResponsible, null=True, on_delete=models.PROTECT, verbose_name="Person/Company responsible") 
    
    def __str__(self):
        return self.company_name

