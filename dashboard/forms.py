
from django.db.models.base import Model
from django.forms import ModelForm, widgets, FileInput
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit


from dashboard.models import (
    DashboardModel,
    AreaOfIssue,
    Locations,
    PersonResponsible,
    SupervisorTeam,
    ProductionIssues,
    SupplierIssues,
    CustomerIssues,
    OtherIssues,

)


class RecordForm(ModelForm):

    
    class Meta:
        model = DashboardModel
        
       # widgets = {'document': FileInput(attrs={'accept': 'file/png, file/jpg'})}
        
        fields = (
            "issue_date", 
            "ncr_number", 
            "job_reference_number",
            "location", 
            "area", 
            "cost",
            "client",
            "issue_solved", 
            "closure_date", 
            "target_completion_date",
            "estimated_completion_time", 
            "advice_number",
            "downtime_time",
            "the_subject_responsible", 
            "supervisor",
            "description", 
            "comments", 
            "root_cause", 
            "interim_containment_action", 
            "corrective_action", 
            "result_validation_action", 
            "issue_affect_other_areas", 
            "issue_affect_other_areas_description",
            "prevented_reoccurrence", 
            "image_upload",
            "ncr_creator",
            "severity",
            "production_issue",
            "supplier_issue",
            "customer_issues",
            "other_issues",
            "area_in_specific",
            "severity",
            "printed_by",
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
            "target_completion_date" : "Target Completion Date",
            "estimated_completion_time" : "Estimated Completion Time", 
            "advice_number" : "Advice Number",
            "downtime_time" : "Downtime",
            "the_subject_responsible" : "Person/Company Responsible", 
            "supervisor" : "Supervisor",
            "description" : "Description", 
            "root_cause" : "Root Cause", 
            "interim_containment_action" : "Interim Containment Action", 
            "corrective_action" : "Corrective Action", 
            "result_validation_action" : "Result of the Validation Action", 
            "issue_affect_other_areas" : "Issue Affect Other Areas", 
            "issue_affect_other_areas_description" : "Issue Affect Other Areas Description",
            "prevented_reoccurrence" : "Prevented Reoccurrence", 
            "image_upload" : "Images",
            "production_issue" : "Production issues" ,
            "supplier_issue" : "Supplier issues" ,
            "customer_issues" : "Customer issues" ,
            "other_issues" : "Other issues" ,
            "area_in_specific" : "Specific area of issue",
            "client" : "Client" ,
            "ncr_creator" : "NCR Creator" ,
            "comments" : "Comments" ,
            "severity" : "Severity" ,
            "printed_by" : "Quality Engineering Team"

            }
        
        
        widgets = {
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
            "target_completion_date" : forms.TextInput( attrs={
            'class':'form-control' ,
            'id':'inputDate' , 
            'type':'date' ,  
            'onclick' : 'showPicker()'
            }),  
            "estimated_completion_time" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Total Completion time'}),
            "downtime_time" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Total Downtime'}),
            'the_subject_responsible': forms.CheckboxSelectMultiple(attrs={}),
            'supervisor': forms.CheckboxSelectMultiple(attrs={}),
            "description" :  forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}), 
            "root_cause" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Root Cause'}),
            "interim_containment_action" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'interim_containment_action'}), 
            "corrective_action" : forms.Textarea(attrs={'class':'form-control', 'placeholder':'corrective_action'}), 
            "advice_number" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'advice_number'}), 
            "result_validation_action" :  forms.Textarea(attrs={'class':'form-control', 'placeholder':'result_validation_action'}), 
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
            "image_upload" : forms.ClearableFileInput(attrs={'class':'form-control form-control-lg', 'placeholder':'images' }),

            "production_issue" : forms.CheckboxSelectMultiple(attrs={}),
            "supplier_issue" : forms.CheckboxSelectMultiple(),
            "customer_issues" : forms.CheckboxSelectMultiple(),
            "other_issues" : forms.CheckboxSelectMultiple(),
            "area_in_specific" : forms.CheckboxSelectMultiple(),
            
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
            "printed_by": forms.SelectMultiple(attrs={'class':'form-control'}),

            }
        
        
