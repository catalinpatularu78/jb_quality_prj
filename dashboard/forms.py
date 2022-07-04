
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit


from dashboard.models import DashboardModel


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
            "issue_solved", 
            "closure_date", 
            "estimated_completion_time", 
            "advice_number",
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
            "advice_number" : "Advice Number",
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
            "advice_number" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'advice_number'}), 
            "result_validation_action" :  forms.Textarea(attrs={'class':'form-control', 'placeholder':'result_validation_action'}), 
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