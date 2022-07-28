# dashboard URL file 
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path , include
from django.contrib.auth.views import LogoutView
from .report_generator import Report
from .views import DashboardModel

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

def generate_report_name():
       '''the ncr number soon won't be taken from DashboardModel, 
       it will be taken from a new form where user is asked to type ncr number
       before generating pdf'''
       
       report_name = DashboardModel.objects.latest('ncr_number')
       return str(report_name) + ".pdf"

urlpatterns = [

    
    path('', HomePage.as_view(),  name= 'main_page'),
    path('login/', CustomLoginView.as_view(),  name= 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    path('dashboard/', DashboardPage.as_view(),  name= 'dashboard'),
    path('filter_dashboard/', FilterDashboardPage.as_view(),  name= 'filter_dashboard'),
    
    path('dashboard/record_create/', RecordCreatePage.as_view(),  name= 'record_create'),
    path("dashboard/record_details/<str:pk>/", RecordDetailPage.as_view(), name="record_detail"),
    path('dashboard/record_update/<str:pk>/', RecordUpdatePage.as_view(),  name= 'record_update'),
    path('dashboard/record_delete/<str:pk>', RecordDeletePage.as_view(),  name= 'record_delete'),

    path('dashboard/production_issue_update/', IssueFormPage.as_view(),  name= 'production_issue_update'),
    
    path(generate_report_name(), Report.generate, name='run_pdfgen'),
    



    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)