from django.contrib import admin

# Register your models here.
from .models import (
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

admin.site.register(DashboardModel)
admin.site.register(AreaOfIssue)
admin.site.register(Locations)
admin.site.register(Employees)
admin.site.register(SupervisorTeam)
admin.site.register(ProductionIssues)
admin.site.register(JandBIssues)
admin.site.register(SupplierIssues)
admin.site.register(CustomerIssues)
admin.site.register(OtherIssues)
