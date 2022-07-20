import django_filters
from django_filters import DateFilter, CharFilter

from .models import *
from django import forms
from django.forms import widgets


class DashboardFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="issue_date", lookup_expr='gte')
	end_date = DateFilter(field_name="issue_date", lookup_expr='lte')
	note = CharFilter(field_name='note', lookup_expr='icontains')


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
        "downtime_time"
        )
		