# dashboard URL file 
from pickle import OBJ
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .report_gen import Report
from django.http import HttpResponseRedirect
from django.urls import reverse


from .views import (
    HomePage,
    CustomLoginView,
    DashboardPage,
    RecordDetailPage,
    RecordCreatePage,
    RecordUpdatePage,
    RecordDeletePage,
    IssueFormPage,
    FilterDashboardPage,
)



urlpatterns = [

    
    path('', HomePage.as_view(),  name= 'main_page'),
    path('login/', CustomLoginView.as_view(),  name= 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    path('dashboard/', DashboardPage.as_view(),  name= 'dashboard'),
    path('filter_dashboard/', FilterDashboardPage.as_view(),  name= 'filter_dashboard'),
    
    path('dashboard/record_create/', RecordCreatePage.as_view(),  name= 'record_create'),
    path('dashboard/record_details/<str:pk>/', RecordDetailPage.as_view(), name="record_detail"),
    path('dashboard/record_update/<str:pk>/', RecordUpdatePage.as_view(),  name= 'record_update'),
    path('dashboard/record_delete/<str:pk>', RecordDeletePage.as_view(),  name= 'record_delete'),

    path('dashboard/production_issue_update/', IssueFormPage.as_view(),  name= 'production_issue_update'),

    path('record_details/<str:pk>/report.pdf', Report.generate, name='run_pdfgen'),
  
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



def redirect_to_main(request):
    # ...
    main = "report.pdf"
    # ...
    return HttpResponseRedirect(reverse('run_pdfgen', args=(main,)))