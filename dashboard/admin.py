from django.contrib import admin
from django.urls import reverse
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect




# Register your models here.
from .models import (
    DashboardModel,
    AreaOfIssue,
    JBClient,
    PersonResponsible,
    QualityEngineerTeam,
    SpecificAreaOfIssue,
    Locations,
    SupervisorTeam,
    ProductionIssues,
    SupplierIssues,
    CustomerIssues,
    OtherIssues,
    ClientModel,

    #ManyToOne
    Employee,
    Supplier,
    Customer,
    ProductionCompany,
    DeliveryPartner,
    OtherCompany,
)



# bulk csv uploads
class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()




class ClientAdmin(admin.ModelAdmin):
    list_display = ['name']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            # [:-1] returns blank line at end , slice option 
            for x in csv_data:
                if x == "" : continue
                fields = x.split(",")
                created = JBClient.objects.update_or_create(
                    name = fields[0]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


class CompanyResponsibleAdmin(admin.ModelAdmin):
    list_display = ['name']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            # [:-1] returns blank line at end , slice option 
            for x in csv_data:
                if x == "" : continue
                fields = x.split(",")

                obj, created = ClientModel.objects.update_or_create(
                    name = fields[0]
                    )
                if not created:
                    messages.warning(request, "Duplicate entry detected: {} already exists.".format(fields[0]))
 

            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


    
    def save_model(self, request, obj, form, change):
        exists = ClientModel.objects.filter(name=obj.name).exclude(pk=obj.pk).exists()
        if exists:
            messages.warning(request, f"Duplicate entry detected: {obj.name} already exists.")
        else:
            super().save_model(request, obj, form, change)



class SpecificAreaOfIssueAdmin(admin.ModelAdmin):
    list_display = ['name']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            # [:-1] returns blank line at end , slice option 
            for x in csv_data:
                if x == "" : continue
                fields = x.split(",")
                created = SpecificAreaOfIssue.objects.update_or_create(
                    name = fields[0]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


class AreaOfIssueAdmin(admin.ModelAdmin):
    list_display = ['name']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            # [:-1] returns blank line at end , slice option 
            for x in csv_data:
                if x == "" : continue
                fields = x.split(",")
                created = AreaOfIssue.objects.update_or_create(
                    name = fields[0]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)
    
    
class ProductionIssuesAdmin(admin.ModelAdmin):
    list_display = ['issue_area_name']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            # [:-1] returns blank line at end , slice option 
            for x in csv_data:
                if x == "" : continue
                fields = x.split(",")
                created = ProductionIssues.objects.update_or_create(
                    issue_area_name = fields[0]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


class SupplierIssuesAdmin(admin.ModelAdmin):
    list_display = ['issue_area_name']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            # [:-1] returns blank line at end , slice option 
            for x in csv_data:
                if x == "" : continue
                fields = x.split(",")
                created = SupplierIssues.objects.update_or_create(
                    issue_area_name = fields[0]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

class CustomerIssuesAdmin(admin.ModelAdmin):
    list_display = ['issue_area_name']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            # [:-1] returns blank line at end , slice option 
            for x in csv_data:
                if x == "" : continue
                fields = x.split(",")
                created = CustomerIssues.objects.update_or_create(
                    issue_area_name = fields[0]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

class OtherIssuesAdmin(admin.ModelAdmin):
    list_display = ['issue_area_name']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            # [:-1] returns blank line at end , slice option 
            for x in csv_data:
                if x == "" : continue
                fields = x.split(",")
                created = OtherIssues.objects.update_or_create(
                    issue_area_name = fields[0]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)
    
    
    
class LocationsAdmin(admin.ModelAdmin):
    list_display = ['name']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            # [:-1] returns blank line at end , slice option 
            for x in csv_data:
                if x == "" : continue
                fields = x.split(",")
                created = Locations.objects.update_or_create(
                    name = fields[0]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

class SupervisorTeamAdmin(admin.ModelAdmin):
    list_display = ['name']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            # [:-1] returns blank line at end , slice option 
            for x in csv_data:
                if x == "" : continue
                fields = x.split(",")
                created = SupervisorTeam.objects.update_or_create(
                    name = fields[0]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


class QualityEngineerTeamAdmin(admin.ModelAdmin):
    list_display = ['name']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            # [:-1] returns blank line at end , slice option 
            for x in csv_data:
                if x == "" : continue
                fields = x.split(",")
                created = QualityEngineerTeam.objects.update_or_create(
                    name = fields[0]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)


class PersonResponsibleAdmin(admin.ModelAdmin):
    list_display = ['title']

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            
            # [:-1] returns blank line at end , slice option 
            for x in csv_data:
                if x == "" : continue
                fields = x.split(",")
                created = PersonResponsible.objects.update_or_create(
                    title = fields[0]
                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)



#ManyToMany
admin.site.register(DashboardModel)
admin.site.register(AreaOfIssue, AreaOfIssueAdmin)
admin.site.register(SpecificAreaOfIssue, SpecificAreaOfIssueAdmin)
admin.site.register(Locations, LocationsAdmin)
admin.site.register(SupervisorTeam, SupervisorTeamAdmin)
admin.site.register(QualityEngineerTeam, QualityEngineerTeamAdmin)
admin.site.register(ProductionIssues, ProductionIssuesAdmin)
admin.site.register(SupplierIssues, SupplierIssuesAdmin)
admin.site.register(CustomerIssues, CustomerIssuesAdmin)
admin.site.register(OtherIssues, OtherIssuesAdmin)
admin.site.register(PersonResponsible, PersonResponsibleAdmin) 
admin.site.register(ClientModel, CompanyResponsibleAdmin) 
admin.site.register(JBClient, ClientAdmin)

#ManyToOne
admin.site.register(Employee)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(ProductionCompany)
admin.site.register(DeliveryPartner)
admin.site.register(OtherCompany)


