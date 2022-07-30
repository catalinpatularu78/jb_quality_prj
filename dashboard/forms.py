
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
<<<<<<< HEAD
from django.core.validators import MaxValueValidator, MinValueValidator
=======
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit


<<<<<<< HEAD
from dashboard.models import (
    DashboardModel,
    AreaOfIssue,
    Locations,
    Employees,
    SupervisorTeam,
    ProductionIssues,
    SupplierIssues,
    CustomerIssues,
    OtherIssues,

)
=======
from dashboard.models import DashboardModel
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3


class RecordForm(ModelForm):

    
    class Meta:
        model = DashboardModel
        
        fields = (
            "issue_date", 
            "ncr_number", 
            "job_reference_number",
            "location", 
            "area", 
            "cost",
<<<<<<< HEAD
            "client",
=======
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
            "issue_solved", 
            "closure_date", 
            "estimated_completion_time", 
            "advice_number",
            "downtime_time",
            "employee", 
            "supervisor",
            "description", 
<<<<<<< HEAD
            "comments", 
=======
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
            "root_cause", 
            "interim_containment_action", 
            "corrective_action", 
            "result_validation_action", 
            "issue_affect_other_areas", 
            "issue_affect_other_areas_description",
            "prevented_reoccurrence", 
            "images",
<<<<<<< HEAD
            "ncr_creator",
            "severity",
            "production_issue",
            "supplier_issue",
            "customer_issues",
            "other_issues",
            "severity",
=======
            "ncr_hyperlink",
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
        )
        
        labels = {
            "issue_date" : "Issue Date", 
            "ncr_number" : "NCR Number", 
            "job_reference_number" : "Job Reference Number",
            "location" : "Location", 
            "area" : "Area", 
            "cost" : "Cost",
            "issue_solved" : "Issue Solved", 
            "closure_date" : "Closure Date", 
            "estimated_completion_time" : "Estimated Completion Time", 
            "advice_number" : "Advice Number",
            "downtime_time" : "Downtime",
            "employee" : "Person Responsible", 
            "supervisor" : "Supervisor",
            "description" : "Description", 
            "root_cause" : "Root Cause", 
            "interim_containment_action" : "Interim Containment Action", 
            "corrective_action" : "Corrective Action", 
<<<<<<< HEAD
            "result_validation_action" : "Result of the Validation Action", 
=======
            "result_validation_action" : "Result Validation Action", 
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
            "issue_affect_other_areas" : "Issue Affect Other Areas", 
            "issue_affect_other_areas_description" : "Issue Affect Other Areas Description",
            "prevented_reoccurrence" : "Prevented Reoccurrence", 
            "images" : "Images",
<<<<<<< HEAD
            "production_issue" : "Production issues" ,
            "supplier_issue" : "Supplier issues" ,
            "customer_issues" : "Customer issues" ,
            "other_issues" : "Other issues" ,
            "client" : "Client" ,
            "ncr_creator" : "NCR Creator" ,
            "comments" : "Comments" ,
            "severity" : "Severity" ,

=======
            "ncr_hyperlink" : "NCR hyperlink",
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
            }
        
        
        widgets = {
<<<<<<< HEAD
            "issue_date" : forms.TextInput( attrs={
                    'class':'form-control' ,
                    'id':'inputDate' , 
                    'type':'datetime-local' ,  
                    'onclick' : 'showPicker()',
                    
                    }), 
            "ncr_number" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'NCR Number'}),
            "job_reference_number" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Reference Number'}),
            'location': forms.CheckboxSelectMultiple(attrs={ }),
            'area': forms.CheckboxSelectMultiple(), 
            "cost" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cost'}),
            "issue_solved" :  forms.Select(attrs={'class':'form-select', 'placeholder':'Issue Resolved'}),
            "closure_date" : forms.TextInput( attrs={
                    'class':'form-control' ,
                    'id':'inputDate' , 
                    'type':'date' ,  
                    'onclick' : 'showPicker()'
                    }),  
            "estimated_completion_time" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Total Completion time'}),
            "downtime_time" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Total Downtime'}),
            'employee': forms.CheckboxSelectMultiple(attrs={}),
            'supervisor': forms.CheckboxSelectMultiple(attrs={}),
            "description" :  forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}), 
            "root_cause" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Root Cause'}),
=======
            "issue_date" : forms.DateInput( attrs={
                    'class':'form-control' ,
                    'id':'inputDate' , 
                    'type':'date' , 
                    'placeholder':'Issue Date' , 
                    'onclick' : 'showPicker()'
                    }), 
            "ncr_number" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'NCR Number'}),
            "job_reference_number" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Reference Number'}),
            'location': forms.CheckboxSelectMultiple(),
            'area': forms.CheckboxSelectMultiple(), 
            "cost" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cost'}),
            "issue_solved" :  forms.Select(attrs={'class':'form-select', 'placeholder':'Issue Resolved'}),
            "closure_date" : forms.DateInput(attrs={'class':'form-control' ,'id':'inputDate' , 'type':'date' , 'placeholder':'Issue Date' }), 
            "estimated_completion_time" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cost'}),
            "downtime_time" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Downtime'}),
            'employee': forms.CheckboxSelectMultiple(),
            'supervisor': forms.CheckboxSelectMultiple(),
            "description" :  forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}), 
            "root_cause" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'NCR Number'}),
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
            "interim_containment_action" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'interim_containment_action'}), 
            "corrective_action" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'corrective_action'}), 
            "advice_number" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'advice_number'}), 
            "result_validation_action" :  forms.Textarea(attrs={'class':'form-control', 'placeholder':'result_validation_action'}), 
<<<<<<< HEAD
            "issue_affect_other_areas" :  forms.Select(
                choices= [
                    ("", "Please choose"),
                    ("yes", "Yes"),
                    ("no", "No"),
                    ],
                attrs={'class':'form-select', 'placeholder':'issue_affect_other_areas',}
                ), 
            "issue_affect_other_areas_description" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'issue_affect_other_areas_description'}),
            "prevented_reoccurrence" : forms.Select(attrs={'class':'form-select', 'placeholder':'prevented_reoccurrence'}),
            "images" : forms.ClearableFileInput(attrs={'class':'form-control form-control-lg " id="formFileLg" type="file', 'placeholder':'images'}),

            "production_issue" : forms.CheckboxSelectMultiple(attrs={}),
            "supplier_issue" : forms.CheckboxSelectMultiple(),
            "customer_issues" : forms.CheckboxSelectMultiple(),
            "other_issues" : forms.CheckboxSelectMultiple(),
            
            "client" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'client'}) ,
            "ncr_creator" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'ncr_creator'}) ,
            "comments" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Comments'}), 
            "severity" : forms.Select(
                choices= [
                    ("", "Please choose"),
                    (1, "1 - LOW"),
                    (2, "2  - MEDIUM"),
                    (3, "3  - HIGH"),
                    ],
                attrs={'class':'form-select', 'placeholder':'severity',}
                ),
            
            
            }
        
        
=======
            "issue_affect_other_areas" :  forms.TextInput(attrs={'class':'form-control', 'placeholder':'issue_affect_other_areas'}), 
            "issue_affect_other_areas_description" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'issue_affect_other_areas_description'}),
            "prevented_reoccurrence" : forms.Select(attrs={'class':'form-select', 'placeholder':'prevented_reoccurrence'}),
            "images" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'images'}),
            "ncr_hyperlink" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'ncr_hyperlink'}),
            }
        
        
class UpdateCrispyForm(ModelForm):
    
    class Meta:
        model = DashboardModel
        
        fields = (
            "issue_date", 
            "ncr_number", 
            "job_reference_number",
            "location", 
            "area", 
            "cost",
            "issue_solved", 
            "closure_date", 
            "estimated_completion_time", 
            "downtime_time",
            "employee", 
            "supervisor",
            "description", 
            "root_cause", 
            "interim_containment_action", 
            "corrective_action", 
            "result_validation_action", 
            "issue_affect_other_areas", 
            "issue_affect_other_areas_description",
            "prevented_reoccurrence", 
            "images",
            "ncr_hyperlink",
        )
        
        labels = {
            "issue_date" : "Issue Date", 
            "ncr_number" : "NCR Number", 
            "job_reference_number" : "Job Reference Number",
            "location" : "Location", 
            "area" : "Area", 
            "cost" : "Cost",
            "issue_solved" : "Issue Solved", 
            "closure_date" : "Closure Date", 
            "estimated_completion_time" : "Estimated Completion Time", 
            "downtime_time" : "Downtime",
            "employee" : "Person Responsible", 
            "supervisor" : "Supervisor",
            "description" : "Description", 
            "root_cause" : "Root Cause", 
            "interim_containment_action" : "Interim Containment Action", 
            "corrective_action" : "Corrective Action", 
            "result_validation_action" : "Result Validation Action", 
            "issue_affect_other_areas" : "Issue Affect Other Areas", 
            "issue_affect_other_areas_description" : "Issue Affect Other Areas Description",
            "prevented_reoccurrence" : "Prevented Reoccurrence", 
            "images" : "Images",
            "ncr_hyperlink" : "NCR hyperlink",
            }
        
        
        widgets = {
            "issue_date" : forms.DateInput( attrs={
                    'class':'form-control' ,
                    'id':'inputDate' , 
                    'type':'date' , 
                    'placeholder':'Issue Date' , 
                    'onclick' : 'showPicker()'
                    }), 
            "ncr_number" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'NCR Number'}),
            "job_reference_number" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Reference Number'}),
            'location': forms.CheckboxSelectMultiple(),
            'area': forms.CheckboxSelectMultiple(), 
            "cost" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cost'}),
            "issue_solved" :  forms.Select(attrs={'class':'form-select', 'placeholder':'Issue Resolved'}),
            "closure_date" : forms.DateInput(attrs={'class':'form-control' ,'id':'inputDate' , 'type':'date' , 'placeholder':'Issue Date' }), 
            "estimated_completion_time" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cost'}),
            "downtime_time" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Downtime'}),
            'employee': forms.CheckboxSelectMultiple(),
            'supervisor': forms.CheckboxSelectMultiple(),
            "description" :  forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}), 
            "root_cause" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'NCR Number'}),
            "interim_containment_action" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'interim_containment_action'}), 
            "corrective_action" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'corrective_action'}), 
            "result_validation_action" :  forms.Textarea(attrs={'class':'form-control', 'placeholder':'result_validation_action'}), 
            "issue_affect_other_areas" :  forms.Textarea(attrs={'class':'form-control', 'placeholder':'issue_affect_other_areas'}), 
            "issue_affect_other_areas_description" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'issue_affect_other_areas_description'}),
            "prevented_reoccurrence" : forms.Select(attrs={'class':'form-select', 'placeholder':'prevented_reoccurrence'}),
            "images" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'images'}),
            "ncr_hyperlink" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'ncr_hyperlink'}),
            }
        
        
    @property
    def helper(self):
        helper = FormHelper()
        helper.layout= Layout( HTML('<h1>Edit post</h1>'))
        
        for field in self.Meta().fields:
            helper.layout.append(
                Field( field , wrapper_class= 'row' )
            )
            
        helper.layout.append(Submit('submit', 'Submit your updates' , css_class=('btn_primary p-3')))
        helper.field_class = ' col-9 '
        helper.label_class = ' col-3 align-middle '
        
        return helper
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
