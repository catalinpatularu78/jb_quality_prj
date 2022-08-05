from urllib import request
from django.shortcuts import get_object_or_404, render , redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView  # new
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
    PersonResponsible,
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
    

class HomePage(TemplateView):
    
    template_name = 'index.html'



class DashboardPage(LoginRequiredMixin , ListView):
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
        "severity"
        ]
    paginate_by = 20
    
    context_object_name = 'dashboard'
    


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
    

    
class RecordDetailPage(LoginRequiredMixin, DetailView):
    
    model = DashboardModel
    template_name = "dashboard/record_detail.html"
    context_object_name = 'record'

    # def get(self, *args, **kwargs):  
    #     pk = self.kwargs.get('pk')
    #     record = DashboardModel.objects.get(pk=pk)
    #     self.object = self.get_object()

    #     # print("test....", pk)
    #     # print("test....", record.ncr_number)

    #     return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.get_object().id

        record = DashboardModel.objects.get(id=pk)

        names_list = [str(name) for name in record.the_subject_responsible.all()]
        person_responsible = ', '.join(names_list)
        
        subject_information = ""
        area_of_subject = ""

        if(person_responsible != ""):         
            p = PersonResponsible.objects.get(title=person_responsible) 

            data_in_supplier = [str(info) for info in p.supplier_set.all()] 

            if(data_in_supplier): 
                area_of_subject = "Supplier"
                subject_information = ''.join(data_in_supplier)


            data_in_delivery_partner = [str(info) for info in p.deliverypartner_set.all()]
            
            if(data_in_delivery_partner):
                area_of_subject = "Delivery Partner"
                subject_information = ''.join(data_in_delivery_partner)


            data_in_customer = [str(info) for info in p.customer_set.all()] 
            
            if(data_in_customer): 
                area_of_subject = "Customer"
                subject_information = ''.join(data_in_customer)


            data_in_production_company = [str(info) for info in p.productioncompany_set.all()] 
            
            if(data_in_production_company): 
                area_of_subject = "Production"
                subject_information = ''.join(data_in_production_company)


            data_in_other_company = [str(info) for info in p.othercompany_set.all()] 
            
            if(data_in_other_company): 
                area_of_subject = "Other"
                subject_information = ''.join(data_in_other_company)


            data_in_employee = [str(info) for info in p.employee_set.all()] 
            
            if(data_in_employee): 
                area_of_subject = "Employee"
                subject_information = "Internal Employee"
        
        context['company_category'] = area_of_subject
        context['company_name'] = subject_information

        return context
    
    



    
class RecordCreatePage(LoginRequiredMixin , CreateView):
    model = DashboardModel
    template_name = "dashboard/record_create.html"
    form_class = RecordForm
    success_url = reverse_lazy("dashboard")
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
    



    


class RecordDeletePage( StaffMemberRequiredMixin , LoginRequiredMixin , DeleteView):
    
    model = DashboardModel
    template_name = "dashboard/record_delete.html"
    success_url = reverse_lazy("dashboard")


class IssueFormPage(LoginRequiredMixin , CreateView):
    
    model = ProductionIssues
    fields = "__all__"
    template_name = "dashboard/production_issue_update.html"
    context_object_name = 'issue'
    success_url = reverse_lazy("production_issue_update")
    

    def get_context_data(self, **kwargs):
        kwargs['issue_items'] = self.model.objects.all()
        return super(IssueFormPage, self).get_context_data(**kwargs)
    

    
