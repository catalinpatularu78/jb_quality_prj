from django.db import models
from rest_framework import serializers
#    from dashboard.models import DashboardModel
from .models import DashboardModel, SpecificAreaOfIssue, AreaOfIssue, ProductionIssues, \
    SupplierIssues, CustomerIssues, OtherIssues, Locations, SupervisorTeam, QualityEngineerTeam, \
    PersonResponsible, ClientModel, JBClient



#    class CustomDateField(serializers.ReadOnlyField):
#        def to_representation(self, value):
#            if value:
#                return value.date()
#            return None
    
    
#    class DashboardModelSerializer(serializers.ModelSerializer):
#        target_completion_date = serializers.DateField()

#        class Meta:
#            model = DashboardModel
        #    fields = '__all__'  # Include all fields from the model
#        fields = ['ncr_number', 'ncr_creator', 'issue_date', 'root_cause', 'description', 'severity' ]  # Include all fields from the model
        # If you want to include specific fields, you can use a list of field names instead, like: fields = ['id', 'area', 'client', ...]




class SpecificAreaOfIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificAreaOfIssue
        fields = '__all__'

class AreaOfIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaOfIssue
        fields = '__all__'

class ProductionIssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionIssues
        fields = '__all__'

class SupplierIssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierIssues
        fields = '__all__'

class CustomerIssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerIssues
        fields = '__all__'

class OtherIssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherIssues
        fields = '__all__'

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'

class SupervisorTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupervisorTeam
        fields = '__all__'

class QualityEngineerTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityEngineerTeam
        fields = '__all__'

class PersonResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonResponsible
        fields = '__all__'

class ClientModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'

class JBClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = JBClient
        fields = '__all__'

"""
class DashboardModelSerializer(serializers.ModelSerializer):
    area_names = serializers.SerializerMethodField()
    area_names2 = serializers.SerializerMethodField()
    area_names3 = serializers.SerializerMethodField()
    client_names = serializers.SerializerMethodField()
    client_names2 = serializers.SerializerMethodField()
    client_names3 = serializers.SerializerMethodField()
    jb_client_names = serializers.SerializerMethodField()
    jb_client_names2 = serializers.SerializerMethodField()
    jb_client_names3 = serializers.SerializerMethodField()
    location_names = serializers.SerializerMethodField()
    location_names2 = serializers.SerializerMethodField()
    location_names3 = serializers.SerializerMethodField()
    supervisor_names = serializers.SerializerMethodField()
    supervisor_names2 = serializers.SerializerMethodField()
    supervisor_names3 = serializers.SerializerMethodField()
    the_subject_responsible_names = serializers.SerializerMethodField()
    the_subject_responsible_names2 = serializers.SerializerMethodField()
    the_subject_responsible_names3 = serializers.SerializerMethodField()
    production_issue_names = serializers.SerializerMethodField()
    production_issue_names2 = serializers.SerializerMethodField()
    production_issue_names3 = serializers.SerializerMethodField()
    supplier_issue_names = serializers.SerializerMethodField()
    supplier_issue_names2 = serializers.SerializerMethodField()
    supplier_issue_names3 = serializers.SerializerMethodField()
    customer_issues_names = serializers.SerializerMethodField()
    customer_issues_names2 = serializers.SerializerMethodField()
    customer_issues_names3 = serializers.SerializerMethodField()
    other_issues_names = serializers.SerializerMethodField()
    other_issues_names2 = serializers.SerializerMethodField()
    other_issues_names3 = serializers.SerializerMethodField()
    area_in_specific_names = serializers.SerializerMethodField()
    area_in_specific_names2 = serializers.SerializerMethodField()
    area_in_specific_names3 = serializers.SerializerMethodField()
    printed_by_names = serializers.SerializerMethodField()
    printed_by_names2 = serializers.SerializerMethodField()
    printed_by_names3 = serializers.SerializerMethodField()
    
    
    
    
    # Methods for area_names
    def get_area_names(self, obj):
        return self.get_item(obj.area.all(), 0)
    def get_area_names2(self, obj):
        return self.get_item(obj.area.all(), 1)
    def get_area_names3(self, obj):
        return self.get_item(obj.area.all(), 2, True)

    # Methods for client_names
    def get_client_names(self, obj):
        return self.get_item(obj.client.all(), 0)
    def get_client_names2(self, obj):
        return self.get_item(obj.client.all(), 1)
    def get_client_names3(self, obj):
        return self.get_item(obj.client.all(), 2, True)

    # Methods for jb_client_names
    def get_jb_client_names(self, obj):
        return self.get_item(obj.jb_client.all(), 0)
    def get_jb_client_names2(self, obj):
        return self.get_item(obj.jb_client.all(), 1)
    def get_jb_client_names3(self, obj):
        return self.get_item(obj.jb_client.all(), 2, True)

    # Methods for location_names
    def get_location_names(self, obj):
        return self.get_item(obj.location.all(), 0)
    def get_location_names2(self, obj):
        return self.get_item(obj.location.all(), 1)
    def get_location_names3(self, obj):
        return self.get_item(obj.location.all(), 2, True)

    # Methods for supervisor_names
    def get_supervisor_names(self, obj):
        return self.get_item(obj.supervisor.all(), 0)
    def get_supervisor_names2(self, obj):
        return self.get_item(obj.supervisor.all(), 1)
    def get_supervisor_names3(self, obj):
        return self.get_item(obj.supervisor.all(), 2, True)

    # Methods for the_subject_responsible_names
    def get_the_subject_responsible_names(self, obj):
        return self.get_item(obj.the_subject_responsible.all(), 0)
    def get_the_subject_responsible_names2(self, obj):
        return self.get_item(obj.the_subject_responsible.all(), 1)
    def get_the_subject_responsible_names3(self, obj):
        return self.get_item(obj.the_subject_responsible.all(), 2, True)

    # Methods for production_issue_names
    def get_production_issue_names(self, obj):
        return self.get_item(obj.production_issue.all(), 0)
    def get_production_issue_names2(self, obj):
        return self.get_item(obj.production_issue.all(), 1)
    def get_production_issue_names3(self, obj):
        return self.get_item(obj.production_issue.all(), 2, True)

    # Methods for supplier_issue_names
    def get_supplier_issue_names(self, obj):
        return self.get_item(obj.supplier_issue.all(), 0)
    def get_supplier_issue_names2(self, obj):
        return self.get_item(obj.supplier_issue.all(), 1)
    def get_supplier_issue_names3(self, obj):
        return self.get_item(obj.supplier_issue.all(), 2, True)

    # Methods for customer_issues_names
    def get_customer_issues_names(self, obj):
        return self.get_item(obj.customer_issues.all(), 0)
    def get_customer_issues_names2(self, obj):
        return self.get_item(obj.customer_issues.all(), 1)
    def get_customer_issues_names3(self, obj):
        return self.get_item(obj.customer_issues.all(), 2, True)

    # Methods for other_issues_names
    def get_other_issues_names(self, obj):
        return self.get_item(obj.other_issues.all(), 0)
    def get_other_issues_names2(self, obj):
        return self.get_item(obj.other_issues.all(), 1)
    def get_other_issues_names3(self, obj):
        return self.get_item(obj.other_issues.all(), 2, True)
    
    # Methods for area_in_specific_names
    def get_area_in_specific_names(self, obj):
        return self.get_item(obj.area_in_specific.all(), 0)
    def get_area_in_specific_names2(self, obj):
        return self.get_item(obj.area_in_specific.all(), 1)
    def get_area_in_specific_names3(self, obj):
        return self.get_item(obj.area_in_specific.all(), 2, True)
    

    
    def get_item(self, items, index, join_remaining=False):
        if join_remaining and len(items) > index:
            return ', '.join(map(str, items[index:]))
        else:
            return str(items[index]) if len(items) > index else None
"""


class DashboardModelSerializer(serializers.ModelSerializer):
    area_names = serializers.SerializerMethodField()
    client_names = serializers.SerializerMethodField()
    jb_client_names = serializers.SerializerMethodField()
    location_names = serializers.SerializerMethodField()
    supervisor_names = serializers.SerializerMethodField()
    the_subject_responsible_names = serializers.SerializerMethodField()
    production_issue_names = serializers.SerializerMethodField()
    supplier_issue_names = serializers.SerializerMethodField()
    customer_issues_names = serializers.SerializerMethodField()
    other_issues_names = serializers.SerializerMethodField()
    area_in_specific_names = serializers.SerializerMethodField()
    printed_by_names = serializers.SerializerMethodField()
  
 
    
    # Methods for area_names
    def get_area_names(self, obj):
        return ', '.join([item.name for item in obj.area.all()])

    # Methods for client_names
    def get_client_names(self, obj):
        return ', '.join([item.name for item in obj.client.all()])

    # Methods for jb_client_names
    def get_jb_client_names(self, obj):
        return ', '.join([item.name for item in obj.jb_client.all()])

    # Methods for location_names
    def get_location_names(self, obj):
        return ', '.join([item.name for item in obj.location.all()])

    # Methods for supervisor_names
    def get_supervisor_names(self, obj):
        return ', '.join([item.name for item in obj.supervisor.all()])

    # Methods for the_subject_responsible_names
    def get_the_subject_responsible_names(self, obj):
#        return ', '.join([item.name for item in obj.the_subject_responsible.all()])
        return ', '.join([item.title for item in obj.the_subject_responsible.all()])

    # Methods for production_issue_names
    def get_production_issue_names(self, obj):
#       return ', '.join([item.name for item in obj.production_issue.all()])
        return ', '.join([item.issue_area_name for item in obj.production_issue.all()])

    # Methods for supplier_issue_names
    def get_supplier_issue_names(self, obj):
#        return ', '.join([item.name for item in obj.supplier_issue.all()])
        return ', '.join([item.issue_area_name for item in obj.supplier_issue.all()])

    # Methods for customer_issues_names
    def get_customer_issues_names(self, obj):
#        return ', '.join([item.name for item in obj.customer_issues.all()])
        return ', '.join([item.issue_area_name for item in obj.customer_issues.all()])

    # Methods for other_issues_names
    def get_other_issues_names(self, obj):
#        return ', '.join([item.name for item in obj.other_issues.all()])
        return ', '.join([item.issue_area_name for item in obj.other_issues.all()])
    
    # Methods for area_in_specific_names
    def get_area_in_specific_names(self, obj):
        return ', '.join([item.name for item in obj.area_in_specific.all()])
    
    def get_printed_by_names(self, obj):
        return ', '.join([item.name for item in obj.printed_by.all()])

    
    def get_item(self, items, index, join_remaining=False):
        if join_remaining and len(items) > index:
            return ', '.join(map(str, items[index:]))
        else:
            return str(items[index]) if len(items) > index else None


    class Meta:
        model = DashboardModel
        exclude = [
            'area', 'client', 'jb_client', 'location', 'supervisor', 'the_subject_responsible',
            'production_issue', 'supplier_issue', 'customer_issues', 'other_issues', 'area_in_specific', 'printed_by'
        ]
