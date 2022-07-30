<<<<<<< HEAD


from urllib import request
=======
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponseRedirect


from django.views.generic import View 
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView  # new
<<<<<<< HEAD
from django.urls import reverse_lazy  # new



from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.mixins import UserPassesTestMixin

from dashboard.filters import DashboardFilter

# For sending emails
from django.conf import settings
from django.core.mail import send_mail
    
    
from dashboard.models import (
    DashboardModel,
    AreaOfIssue,
    Locations,
    Employees,
    SupervisorTeam,
    ProductionIssues,
    SupplierIssues,
    CustomerIssues,
    OtherIssues,
)

from dashboard.forms import RecordForm 

from django.shortcuts import get_object_or_404


# Create your views here.

class StaffMemberRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff


class CustomLoginView(LoginView):
    template_name = 'dashboard/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')
    

=======
from django.urls import reverse_lazy
from pyparsing import str_type  # new

from dashboard.models import DashboardModel
from dashboard.forms import RecordForm , UpdateCrispyForm




# Create your views here.

>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
class HomePage(TemplateView):
    
    template_name = 'index.html'



<<<<<<< HEAD
class DashboardPage(LoginRequiredMixin , ListView):
=======
class DashboardPage(ListView):
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
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
<<<<<<< HEAD
        "closure_date",
        "downtime_time"
        "downtime_readability"
        "severity"
        ]
    paginate_by = 20
    
    context_object_name = 'dashboard'
    
    # def get_context_data(self, *args,  **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['formatted_downtime'] = self.downtime_time()

    #     return context


class FilterDashboardPage(LoginRequiredMixin , ListView):
    model = DashboardModel
    form_class = RecordForm
    template_name = 'dashboard/filter_dashboard.html'
    fields = [
        "issue_date", 
        "ncr_number", 
        "advice_number",
        "location", 
        "area",
        "cost",
        "issue_solved", 
        "closure_date",
        "downtime_time"
        "downtime_readability"
        ]
    
    
    
    def get_context_data(self, *args,  **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['myFilter'] = DashboardFilter(self.request.GET, queryset= self.get_queryset())
        return context
    
    
    
    
class RecordDetailPage(LoginRequiredMixin , DetailView):
=======
        "closure_date"
        ]
    paginate_by = 20
    
class RecordDetailPage(DetailView):
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
    model = DashboardModel
    template_name = "dashboard/record_detail.html"
    context_object_name = 'record'

<<<<<<< HEAD
    
    # def time_format_converter(self, minutes):
    #     if minutes == None : return "" 
    #     return ( f'{minutes // 1440} days , {((minutes // 60) % 24)} hours , {minutes % 60} minutes')


    # def get_context_data(self, *args,  **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     downtime = self.get_object().downtime_time
    #     context['formatted_downtime'] = self.time_format_converter(downtime)
    #     return context
    



    
class RecordCreatePage(LoginRequiredMixin , CreateView):
=======
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
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
    model = DashboardModel
    template_name = "dashboard/record_create.html"
    form_class = RecordForm
    success_url = reverse_lazy("dashboard")
<<<<<<< HEAD
    context_object_name = 'record_create'
    
    
    def form_valid(self,form):
        response = super().form_valid(form)
        severity =  form.cleaned_data['severity']
        
        if severity and severity > 2:
            try:
                subject = 'NEW QUALITY RECORD '
                message = f'WARNING SEVERITY LEVEL  = {severity}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['jbdjango@outlook.com']
                send_mail( subject, message, email_from, recipient_list)    
            except:
                pass
        
        return response 

    




class RecordUpdatePage(LoginRequiredMixin , UpdateView):
    
    model = DashboardModel
    template_name = "dashboard/record_update.html"
    form_class = RecordForm
    success_url = reverse_lazy("dashboard")
    context_object_name = 'record'

    
    def get_success_url(self):
        return reverse_lazy('record_detail', kwargs={'pk': self.object.pk})
=======

        
        
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
    
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
    



<<<<<<< HEAD
    


class RecordDeletePage( StaffMemberRequiredMixin , LoginRequiredMixin , DeleteView):
    
=======
class RecordDeletePage(DeleteView):
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
    model = DashboardModel
    template_name = "dashboard/record_delete.html"
    success_url = reverse_lazy("dashboard")


<<<<<<< HEAD
class IssueFormPage(LoginRequiredMixin , CreateView):
    
    model = ProductionIssues
    fields = "__all__"
    template_name = "dashboard/production_issue_update.html"
    context_object_name = 'issue'
    success_url = reverse_lazy("production_issue_update")
    

    def get_context_data(self, **kwargs):
        kwargs['issue_items'] = self.model.objects.all()
        return super(IssueFormPage, self).get_context_data(**kwargs)
    

    
=======
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
