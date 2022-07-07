from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponseRedirect


from django.views.generic import View 
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView  # new
from django.urls import reverse_lazy
from pyparsing import str_type  # new

from dashboard.models import DashboardModel
from dashboard.forms import RecordForm , UpdateCrispyForm




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
        "closure_date"
        ]
    paginate_by = 20
    
class RecordDetailPage(DetailView):
    model = DashboardModel
    template_name = "dashboard/record_detail.html"
    context_object_name = 'record'

    def duration_string(self, value):      
        # using list comprehension to convert number to list of integers
        res = [str(x) for x in str(value)]

        days = res[0] + res[1]
        hours = res[2] + res[3]
        minutes = res[4] + res[5]

        return '{}d {}h {}m'.format(days, hours, minutes)

    def get_context_data(self,**kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        downtime = self.get_object().downtime_time     
        context['formatted_downtime'] = self.duration_string(downtime) 
 
        return context

    
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
    form_class = UpdateCrispyForm
    template_name = "dashboard/record_update.html"

    success_url = reverse_lazy("dashboard")
    
    



class RecordDeletePage(DeleteView):
    model = DashboardModel
    template_name = "dashboard/record_delete.html"
    success_url = reverse_lazy("dashboard")


