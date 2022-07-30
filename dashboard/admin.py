from django.contrib import admin

# Register your models here.
from .models import (
    DashboardModel,
    AreaOfIssue,
    Locations,
    Employees,
    SupervisorTeam,
<<<<<<< HEAD
    ProductionIssues,
    SupplierIssues,
    CustomerIssues,
    OtherIssues,

=======
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
)

admin.site.register(DashboardModel)
admin.site.register(AreaOfIssue)
admin.site.register(Locations)
admin.site.register(Employees)
<<<<<<< HEAD
admin.site.register(SupervisorTeam)
admin.site.register(ProductionIssues)
admin.site.register(SupplierIssues)
admin.site.register(CustomerIssues)
admin.site.register(OtherIssues)
=======
admin.site.register(SupervisorTeam)
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
