# dashboard URL file 
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path , include
from django.contrib.auth.views import LogoutView
from .report_gen import Report
from .views import DashboardModel
from django.http import HttpResponse

from .views import (
    HomePage,
    CustomLoginView,
=======

from django.urls import path

from .views import (
    HomePage,
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
    DashboardPage,
    RecordDetailPage,
    RecordCreatePage,
    RecordUpdatePage,
    RecordDeletePage,
<<<<<<< HEAD
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
    path("dashboard/record_details/<str:pk>/", RecordDetailPage.as_view(), name="record_detail"),
    path('dashboard/record_update/<str:pk>/', RecordUpdatePage.as_view(),  name= 'record_update'),
    path('dashboard/record_delete/<str:pk>', RecordDeletePage.as_view(),  name= 'record_delete'),

    path('dashboard/production_issue_update/', IssueFormPage.as_view(),  name= 'production_issue_update'),


    path('dashboard/record_details/<str:pk>/' + "ncr_report.pdf", Report.generate, name='run_pdfgen'),
    
   
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======

)

urlpatterns = [
    
    path('', HomePage.as_view(),  name= 'main_page'),
    path('dashboard/', DashboardPage.as_view(),  name= 'dashboard'),
    path('dashboard/record_create/', RecordCreatePage.as_view(),  name= 'record_create'),
    path("dashboard/record_details/<str:pk>/", RecordDetailPage.as_view(), name="record_detail"),
    path('dashboard/record_update/<str:pk>/', RecordUpdatePage.as_view(),  name= 'record_update'),
    path('dashboard//record_delete/<str:pk>', RecordDeletePage.as_view(),  name= 'record_delete'),


]
>>>>>>> 0d69fb284d6ad3468a42eb034d9c2256bcc59ed3
