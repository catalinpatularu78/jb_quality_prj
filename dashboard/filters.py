from datetime import timedelta
import django_filters
from django_filters import DateFilter, CharFilter, ChoiceFilter, ModelMultipleChoiceFilter
from .models import *
from django import forms




class EndFilter(django_filters.DateFilter):

    def filter(self, qs, value):
        if value:
            print (value)
            value = value + timedelta( days=1,) #days=1,
            print (value)
        return super(EndFilter, self).filter(qs, value)

class DashboardFilter(django_filters.FilterSet):
    
    start_date = DateFilter(
        field_name="issue_date",
        lookup_expr="gte",
        widget = forms.TextInput
                    (attrs={
                        'class':'form-control' ,
                        'id':'inputDate' , 
                        'type':'date',
                        'onclick' : 'showPicker()',
                        'placeholder' : "Issue Date"
                    }), 
        )
    end_date = EndFilter(
        field_name="issue_date", 
        lookup_expr='lte',
        widget = forms.TextInput
                    (attrs={
                        'class':'form-control' ,
                        'id':'inputDate' , 
                        'type':'date' ,  
                        'onclick' : 'showPicker()',
                        'placeholder' : "End Date"
                    }), 
        )
    advice_number = CharFilter(
        field_name='advice_number',
        lookup_expr='icontains',
        widget = forms.TextInput
            (attrs={
                'class':'form-control',
                'placeholder':'Advice number'
            }),
        )
    ncr_number = CharFilter(
        field_name='ncr_number',
        lookup_expr='icontains',
        widget = forms.TextInput
            (attrs={
                'class':'form-control',
                'placeholder':'NCR number'
            }),
        )
    
    
    issue_solved_type = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    
    issue_solved = ChoiceFilter(
        choices=issue_solved_type,
        field_name='issue_solved',
        widget = forms.Select
            (attrs={
                'class':'form-control',
            }),
        )


    issue_solved = ChoiceFilter(
        choices=issue_solved_type,
        field_name='issue_solved',
        widget = forms.Select
            (attrs={
                'class':'form-control',
                'placeholder':''
            }),
        )
    
    location = ModelMultipleChoiceFilter(
        queryset=Locations.objects.all(),
        field_name='location',
        widget = forms.CheckboxSelectMultiple
            (attrs={
                'class' : '',
            }),
        )
    
    
    area = ModelMultipleChoiceFilter(
        queryset=AreaOfIssue.objects.all(),
        field_name='area',
        widget = forms.CheckboxSelectMultiple
            (attrs={
                'class' : '',
            }),
        )
    
    
    
        
    severity_type = (
                    (1, "1 - LOW"),
                    (2, "2  - MEDIUM"),
                    (3, "3  - HIGH"),
                    )
    
    severity = ChoiceFilter(
        choices=severity_type,
        field_name='severity',
        widget = forms.Select
            (attrs={
                'class':'form-control',
            }),
        )


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

        # widgets = {
        #     "issue_date" : forms.DateInput( attrs={
        #             'class':'form-control' ,
        #             'id':'inputDate' , 
        #             'type':'datetime-local' ,  
        #             'onclick' : 'showPicker()',
        #             'placeholder' : "Issue Date"
        #             }), 
        #     "ncr_number" : forms.NumberInput(attrs={'class':'form-control', 'placeholder':'NCR Number'}),
        #     "advice_number" : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Advice Number'}),
        #     "issue_solved" :  forms.Select(attrs={'class':'form-select', 'placeholder':'Issue Resolved'}),
        # }

        fields = [
        "issue_date", 
        "advice_number",
        "ncr_number",
        "issue_solved", 
        "location", 
        "area",
        "severity",
        
        ]
        
