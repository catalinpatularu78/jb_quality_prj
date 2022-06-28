from django.contrib import admin

# Register your models here.
from .models import (
    DashboardModel,
    AreaOfIssue,
    Locations,
    Employees,
    SupervisorTeam,
)

admin.site.register(DashboardModel)
admin.site.register(AreaOfIssue)
admin.site.register(Locations)
admin.site.register(Employees)
admin.site.register(SupervisorTeam)