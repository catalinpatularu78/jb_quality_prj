from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # new
from django.urls import reverse_lazy  # new

from dashboard.models import DashboardModel




# Create your views here.

class HomePage(View):
    
    def get(self, request, *args, **kwargs): 
        return render(request, 'index.html')


class DashboardPage(ListView):
    model = DashboardModel
    template_name = 'dashboard/dashboard.html'
    fields = [
        "issue_date", 
        "ncr_number", 
        "job_reference_number",
        "location", 
        "area",
        "cost",
        "issue_resolved", 
        "closure_date"
        ]
    
    
class RecordDetailPage(DetailView):
    model = DashboardModel
    template_name = "dashboard/record_detail.html"


class RecordCreatePage(CreateView):
    model = DashboardModel
    template_name = "dashboard/record_create.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")


class RecordUpdatePage(UpdateView):
    model = DashboardModel
    template_name = "dashboard/record_update.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")


class RecordDeletePage(DeleteView):
    model = DashboardModel
    template_name = "dashboard/record_delete.html"
    success_url = reverse_lazy("dashboard")


