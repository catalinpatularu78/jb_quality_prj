import django_filters
from django_filters import DateFilter, CharFilter

from .models import *
from django import forms
from django.forms import widgets


class DashboardFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="issue_date", lookup_expr='gte')
    end_date = DateFilter(field_name="issue_date", lookup_expr='lte')
    note = CharFilter(field_name='ncr_number', lookup_expr='icontains')


    class Meta:
        model = DashboardModel


        fields = (
        "issue_date",  
        "job_reference_number",
        "ncr_number",
        "issue_solved", 
        )

        labels = {
        "issue_date" : "Issue Date",  
        "job_reference_number" : "Job ref. number",
        "ncr_number": "NCR Number",
        "issue_solved" : "Issue solved", 
        }

        widgets = {
            "issue_date" : forms.DateInput( attrs={
                    'class':'form-control' ,
                    'id':'inputDate' , 
                    'type':'datetime-local' ,  
                    'onclick' : 'showPicker()',
                    'placeholder' : "Issue Date"
                    }), 
            "ncr_number" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'NCR Number'}),
            "job_reference_number" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Job Reference Number'}),
            "issue_solved" :  forms.Select(attrs={'class':'form-select', 'placeholder':'Issue Resolved'}),
        }