from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponseRedirect


from django.views.generic import View 
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView  # new
from django.urls import reverse_lazy  # new

from dashboard.models import DashboardModel
from dashboard.forms import RecordForm




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
        "issue_resolved", 
        "closure_date"
        ]
    paginate_by = 20
    
class RecordDetailPage(DetailView):
    model = DashboardModel
    template_name = "dashboard/record_detail.html"
    context_object_name = 'record'


    
class RecordCreatePage(FormView):
    
    template_name = "dashboard/record_create.html"
    form_class = RecordForm
    success_url = reverse_lazy("dashboard")
        
        
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    
    def form_invalid(self, form):
        # print (form['issue_date'].value())
        return redirect('main_page')



class RecordUpdatePage(UpdateView):
    model = DashboardModel
    template_name = "dashboard/record_update.html"
    fields = '__all__'
    success_url = reverse_lazy("dashboard")
    



class RecordDeletePage(DeleteView):
    model = DashboardModel
    template_name = "dashboard/record_delete.html"
    success_url = reverse_lazy("dashboard")


