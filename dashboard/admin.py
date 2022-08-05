from django.contrib import admin
from django.urls import reverse

# Register your models here.
from .models import (
    DashboardModel,
    AreaOfIssue,
    PersonResponsible,
    SpecificAreaOfIssue,
    Locations,
    SupervisorTeam,
    ProductionIssues,
    SupplierIssues,
    CustomerIssues,
    OtherIssues,

    #ManyToOne
    Employee,
    Supplier,
    Customer,
    ProductionCompany,
    DeliveryPartner,
    OtherCompany,
)

#ManyToMany
admin.site.register(DashboardModel)
admin.site.register(AreaOfIssue)
admin.site.register(SpecificAreaOfIssue)
admin.site.register(Locations)
admin.site.register(SupervisorTeam)
admin.site.register(ProductionIssues)
admin.site.register(SupplierIssues)
admin.site.register(CustomerIssues)
admin.site.register(OtherIssues)
admin.site.register(PersonResponsible)

#ManyToOne
admin.site.register(Employee)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(ProductionCompany)
admin.site.register(DeliveryPartner)
admin.site.register(OtherCompany)


