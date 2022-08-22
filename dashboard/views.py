from datetime import datetime
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView  # new
from django.urls import reverse_lazy  # new
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from dashboard.filters import DashboardFilter
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max, Min
from django.db import connection
from django.contrib import messages
#from django.core.exceptions import ValidationError, FieldError
from django.forms import ValidationError

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
    Image,
)

from dashboard.forms import RecordForm, ImageForm


class StaffMemberRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff


class CustomLoginView(LoginView):
    template_name = 'dashboard/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy('dashboard')
        else:
            return reverse_lazy('dashboard_b')


    
class HomePage(TemplateView):
    
    template_name = 'index.html'



class DashboardPage(StaffMemberRequiredMixin , LoginRequiredMixin , ListView):
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


    # def get(self, request, *args, **kwargs):
    #     response = super().get(request, *args, **kwargs)

    #     if not request.user.is_superuser:
    #         return HttpResponse('You do not have required privileges to view this page.')        
    #     else:
    #         return response



class OperativeDashboardPage(StaffMemberRequiredMixin , LoginRequiredMixin , ListView):
    model = DashboardModel
    template_name = 'dashboard/dashboard_b.html'
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


    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        if request.user.is_superuser:
            return HttpResponseRedirect('/dashboard/')        
        else:
            return response
    

class FilterDashboardPage(StaffMemberRequiredMixin, LoginRequiredMixin , ListView):
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
        ]
    
    
    def get_context_data(self, *args,  **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['myFilter'] = DashboardFilter(self.request.GET, queryset= self.get_queryset())
        return context
    


class OperativeFilterDashboardPage(StaffMemberRequiredMixin, LoginRequiredMixin , ListView):
    model = DashboardModel
    form_class = RecordForm
    template_name = 'dashboard/filter_dashboard_b.html'
    fields = [
        "issue_date", 
        "ncr_number", 
        "advice_number",
        "location", 
        "area",
        "cost",
        "issue_solved", 
        ]


    def get_context_data(self, *args,  **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['myFilter'] = DashboardFilter(self.request.GET, queryset= self.get_queryset())
        return context



#decorators = [csrf_exempt]

#@method_decorator(decorators, name='dispatch')
class RecordDetailPage(StaffMemberRequiredMixin, LoginRequiredMixin, DetailView):
    
    model = DashboardModel
    template_name = "dashboard/record_detail.html"
    context_object_name = 'record'

    def form_valid(self,form):         
        response = super().form_valid(form)

        return response


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.get_object().id

        record = DashboardModel.objects.get(id=pk)

        # utc_date_format = "%Y-%m-%d"
        # custom_date_format = "%d/%m/%Y"
        # the_target_completion_date = "None"
        # the_closure_date = "None"
        # if(record.target_completion_date!=None):
        #     timestring = datetime.strptime(str(record.target_completion_date)[:10], utc_date_format) 
        #     the_target_completion_date = str(datetime.fromtimestamp(timestring.timestamp()).strftime(custom_date_format))
        # else:
        #     pass
        
        # if(record.closure_date!=None):
        #     timestring_2 = datetime.strptime(str(record.closure_date)[:10], utc_date_format) 
        #     the_closure_date = str(datetime.fromtimestamp(timestring_2.timestamp()).strftime(custom_date_format))
        # else:
        #     pass

        the_target_completion_date = '{:02d}'.format( int(str(record.target_completion_date)[8:10])+1 ) +'/'+str(record.target_completion_date)[5:7]+'/'+str(record.target_completion_date)[:4]
        the_closure_date = '{:02d}'.format( int(str(record.closure_date)[8:10])+1 ) +'/'+str(record.closure_date)[5:7]+'/'+str(record.closure_date)[:4]

        if(the_target_completion_date!="//None"):
            context['the_target_completion_date'] = the_target_completion_date
        else:
            context['the_target_completion_date'] = "None"

        if(the_closure_date!="//None"):
            context['the_closure_date'] = the_closure_date
        else:
            context['the_closure_date'] = "None"

        names_list = [str(name) for name in record.the_subject_responsible.all()]
        person_responsible = ', '.join(names_list)
        
        subject_information = ""
        area_of_subject = ""

        if("," in person_responsible): #more than one names for the same company type
            person_responsible = person_responsible.split(',')[0]


        if(person_responsible != ""):         
            p = PersonResponsible.objects.get(title=person_responsible) 

            data_in_supplier = [str(info) for info in p.supplier_set.all()] 

            if(data_in_supplier): 
                area_of_subject = "(Type: Supplier)"
                subject_information = ''.join(data_in_supplier)


            data_in_delivery_partner = [str(info) for info in p.deliverypartner_set.all()]
            
            if(data_in_delivery_partner):
                area_of_subject = "(Type: Delivery Partner)"
                subject_information = ''.join(data_in_delivery_partner)


            data_in_customer = [str(info) for info in p.customer_set.all()] 
            
            if(data_in_customer): 
                area_of_subject = "(Type: Customer)"
                subject_information = ''.join(data_in_customer)


            data_in_production_company = [str(info) for info in p.productioncompany_set.all()] 
            
            if(data_in_production_company): 
                area_of_subject = "(Type: Production)"
                subject_information = ''.join(data_in_production_company)


            data_in_other_company = [str(info) for info in p.othercompany_set.all()] 
            
            if(data_in_other_company): 
                area_of_subject = "(Type: Other)"
                subject_information = ''.join(data_in_other_company)


            data_in_employee = [str(info) for info in p.employee_set.all()] 
            
            if(data_in_employee): 
                area_of_subject = ""
                subject_information = "Internal Employee"
        
        context['company_category'] = area_of_subject
        context['company_name'] = subject_information

        return context
    
    

#@method_decorator(decorators, name='dispatch')   
class RecordCreatePage(StaffMemberRequiredMixin,LoginRequiredMixin , CreateView):
    model = DashboardModel
    template_name = "dashboard/record_create.html"
    form_class = RecordForm
    success_url = reverse_lazy("dashboard")
    context_object_name = 'record_create'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['imageform'] = ImageForm
        
        form = RecordForm()      
        record = DashboardModel.objects.first()

        if(record == None):
            context['reset_number'] = "Overwrite NCR Number:"
            context['hardcode_ncr_number'] = form['ncr_number']

        num = 1
        if(record != None):
            num = record.ncr_number + 1
            context['context_number'] = num
        else:
            context['context_number'] = num
 
        return context


    def post(self, request, *args, **kwargs):
        response = super().post(self, request, *args, **kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        files = request.FILES.getlist('image')
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            for i in files:
                Image.objects.create(project=f, image=i)
            messages.success(request, "New image added")

            return self.form_valid(form)
        else:
            print(form.errors)

        return response


    def form_valid(self,form):
        response = super().form_valid(form)
        severity =  form.cleaned_data['severity']

        record_form = form.save(commit=False) # cancel commit to DB

        #auto increment NCR number
        number = DashboardModel.objects.all().aggregate(Max('ncr_number')).get('ncr_number__max') # gets max ncr_number
        record_form.ncr_number = int(number) + 1 if number else 1 # increments max by 1 and max starts at 1
        record_form.save() # saves form


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



class RecordUpdatePage(StaffMemberRequiredMixin, LoginRequiredMixin , UpdateView):
    
    model = DashboardModel
    template_name = "dashboard/record_update.html"
    form_class = RecordForm
    success_url = reverse_lazy("dashboard")
    context_object_name = 'record'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imageform'] = ImageForm

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        tcd = form['target_completion_date']
        cd = form['closure_date']
        the_target_completion_date = str(tcd.value())[8:10]+'/'+str(tcd.value())[5:7]+'/'+str(tcd.value())[:4]
        the_closure_date = str(cd.value())[8:10]+'/'+str(cd.value())[5:7]+'/'+str(cd.value())[:4]
        
        if(the_target_completion_date!="//None"):
            context['the_target_completion_date2'] = the_target_completion_date
        # else:
        #     context['the_target_completion_date2'] = ""

        if(the_closure_date!="//None"):
            context['the_closure_date2'] = the_closure_date
        # else:
        #     context['the_closure_date2'] = ""
            
        return context


    def post(self, request, *args, **kwargs):        
        response = super().post(self, request, *args, **kwargs)
        
        form_class = self.get_form_class()
        form = self.get_form(form_class)
 
        pk = self.get_object().id
        d = DashboardModel.objects.get(id=pk)

        files = request.FILES.getlist('image')
        
        if form.is_valid():           
            f = form.save(commit=False)
            f.user = request.user
            f.save()

            if(d.image_set.all()): #if images are present in the record  
                d.image_set.all().delete()
                for i in files:
                    Image.objects.update_or_create(project=f, image=i)    
            else:
                d.image_set.all().delete()
                for i in files:
                    Image.objects.create(project=f, image=i)   

            messages.success(request, "New images updated")

            return self.form_valid(form) 
        else:
            print(form.errors)
      
        return response
  

    def get_success_url(self):
        return reverse_lazy('record_detail', kwargs={'pk': self.object.pk})
    


class OperativeCreatePage(LoginRequiredMixin , CreateView):
    model = DashboardModel
    template_name = "dashboard/operative_input.html"
    form_class = RecordForm
    success_url = reverse_lazy("dashboard_b")
    context_object_name = 'record_create'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['imageform'] = ImageForm
        
        record = DashboardModel.objects.first()

        num = 1
        if(record != None):
            num = record.ncr_number + 1
            context['context_number'] = num
        else:
            context['context_number'] = num

        return context


    def post(self, request, *args, **kwargs):
        response = super().post(self, request, *args, **kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        files = request.FILES.getlist('image')
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            for i in files:
                Image.objects.create(project=f, image=i)
            messages.success(request, "New image added")

            return self.form_valid(form)
        else:
            print(form.errors)

        return response
    
    
    def form_valid(self,form):
        
        # Auto increment NCR code 
        number = DashboardModel.objects.all().aggregate(Max('ncr_number')).get('ncr_number__max') # gets max ncr_number
        record_form = form.save(commit=False) # cancel commit to DB
        record_form.ncr_number = int(number) + 1 if number else 1 # Sets value to max number plus 1 or 1 if number column is empty 
        record_form.save() # saves form
        
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




class OperativeUpdatePage(StaffMemberRequiredMixin, LoginRequiredMixin , UpdateView):
    
    model = DashboardModel
    template_name = "dashboard/operative_update.html"
    form_class = RecordForm
    success_url = reverse_lazy("dashboard_b")
    context_object_name = 'record'


    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['imageform'] = ImageForm
             
            return context
    

    def post(self, request, *args, **kwargs):
        response = super().post(self, request, *args, **kwargs)
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        pk = self.get_object().id
        d = DashboardModel.objects.get(id=pk)

        files = request.FILES.getlist('image')
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()        
            
            if(d.image_set.all()): #if images are present in the record  
                d.image_set.all().delete()
                for i in files:
                    Image.objects.update_or_create(project=f, image=i)    
            else:
                d.image_set.all().delete()
                for i in files:
                    Image.objects.create(project=f, image=i)  

            messages.success(request, "New images updated")         
        else:
            print(form.errors)

        return response
        


    def get_success_url(self):
        return reverse_lazy('record_detail', kwargs={'pk': self.object.pk})



class RecordDeletePage( StaffMemberRequiredMixin , LoginRequiredMixin , DeleteView):
    
    model = DashboardModel
    template_name = "dashboard/record_delete.html"
    success_url = reverse_lazy("dashboard")

    #unimplemented
    # def get_context_data(self, *args,  **kwargs):

    #     context = super().get_context_data(*args, **kwargs)
        
    #     context['caution_message'] = "Please delete records with higher NCR numbers first"
        
    #     for object in DashboardModel.objects.all():
    #         if object.ncr_number < len(DashboardModel.objects.all()) and object.ncr_number < object.ncr_number + 1:
    #             context['caution_message'] = "Please delete records with higher NCR numbers first"
    #         else:
    #             context['caution_message'] = "placeholder"
  
    #     return context


class IssueFormPage(LoginRequiredMixin , CreateView):
    
    model = ProductionIssues
    fields = "__all__"
    template_name = "dashboard/production_issue_update.html"
    context_object_name = 'issue'
    success_url = reverse_lazy("production_issue_update")
    

    def get_context_data(self, **kwargs):
        kwargs['issue_items'] = self.model.objects.all()
        return super(IssueFormPage, self).get_context_data(**kwargs)
    

    
