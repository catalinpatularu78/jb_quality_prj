
from urllib import request
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponseRedirect


from django.views.generic import View 
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView  # new
from django.urls import reverse_lazy  # new

from dashboard.models import (
    DashboardModel,
    AreaOfIssue,
    Locations,
    Employees,
    SupervisorTeam,
    ProductionIssues,
    JandBIssues,
    SupplierIssues,
    CustomerIssues,
    OtherIssues,
)

from dashboard.forms import RecordForm 

from django.shortcuts import get_object_or_404


# Create your views here.

class HomePage(TemplateView):
    
    template_name = 'index.html'



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
        "issue_solved", 
        "closure_date",
        "downtime_time"
        "downtime_readability"
        
        ]
    paginate_by = 20
    
    context_object_name = 'dashboard'
    
    # def get_context_data(self, *args,  **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['formatted_downtime'] = self.downtime_time()

    #     return context


    
    
    
class RecordDetailPage(DetailView):
    model = DashboardModel
    template_name = "dashboard/record_detail.html"
    context_object_name = 'record'

    
    # def time_format_converter(self, minutes):
    #     if minutes == None : return "" 
    #     return ( f'{minutes // 1440} days , {((minutes // 60) % 24)} hours , {minutes % 60} minutes')


    # def get_context_data(self, *args,  **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     downtime = self.get_object().downtime_time
    #     context['formatted_downtime'] = self.time_format_converter(downtime)
    #     return context
    



    
class RecordCreatePage(CreateView):
    model = DashboardModel
    template_name = "dashboard/record_create.html"
    form_class = RecordForm
    success_url = reverse_lazy("dashboard")
    

        
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    
    # def form_invalid(self, form):
    #     # print (form['issue_date'].value())
    #     return redirect('main_page')



class RecordUpdatePage(UpdateView):
    
    model = DashboardModel
    template_name = "dashboard/record_update.html"
    form_class = RecordForm
    success_url = reverse_lazy("dashboard")
    context_object_name = 'record'

    
    def get_success_url(self):
        return reverse_lazy('record_detail', kwargs={'pk': self.object.pk})
    


class RecordDeletePage(DeleteView):
    model = DashboardModel
    template_name = "dashboard/record_delete.html"
    success_url = reverse_lazy("dashboard")


class IssueFormPage(CreateView):
    
    model = ProductionIssues
    fields = "__all__"
    template_name = "dashboard/production_issue_update.html"
    context_object_name = 'issue'
    success_url = reverse_lazy("production_issue_update")
    

    def get_context_data(self, **kwargs):
        kwargs['issue_items'] = self.model.objects.all()
        return super(IssueFormPage, self).get_context_data(**kwargs)
    

    