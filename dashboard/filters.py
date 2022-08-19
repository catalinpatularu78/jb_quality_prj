import django_filters
from django_filters import DateFilter, CharFilter

from .models import *
from django import forms



class DashboardFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="issue_date", lookup_expr='gte')
    end_date = DateFilter(field_name="issue_date", lookup_expr='lte')
    note = CharFilter(field_name='ncr_number', lookup_expr='icontains')


    class Meta:
        model = DashboardModel


        fields = (
        "issue_date",  
        "advice_number",
        "ncr_number",
        "issue_solved", 
        )

        labels = {
        "issue_date" : "Issue Date",  
        "advice_number" : "Advice no.",
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
            "advice_number" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Advice Number'}),
            "issue_solved" :  forms.Select(attrs={'class':'form-select', 'placeholder':'Issue Resolved'}),
        }