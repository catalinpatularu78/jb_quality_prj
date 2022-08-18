# dashboard URL file 
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LogoutView
from .report_gen import Report


from .views import (
    HomePage,
    OperativeHomePage,
    CustomLoginView,
    DashboardPage,
    OperativeDashboardPage,
    RecordDetailPage,
    RecordCreatePage,
    RecordUpdatePage,
    RecordDeletePage,
    IssueFormPage,
    FilterDashboardPage,
    OperativeFilterDashboardPage,
    OperativeCreatePage,
)



urlpatterns = [

    
    path('', HomePage.as_view(),  name= 'main_page'),

  
    path('home/', OperativeHomePage.as_view(),  name= 'main_b'),   #operative main page

    path('login/', CustomLoginView.as_view(),  name= 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    path('dashboard/', DashboardPage.as_view(),  name= 'dashboard'),
    
    path('dashboard_operative/', OperativeDashboardPage.as_view(),  name= 'dashboard_b'), #operative dashboard page
    path('filter_dashboard_operative/', OperativeFilterDashboardPage.as_view(),  name= 'filter_dashboard_b'), #operative filter
    path('filter_dashboard/', FilterDashboardPage.as_view(),  name= 'filter_dashboard'),
    
 
    path('dashboard/record_create/', RecordCreatePage.as_view(),  name= 'record_create'),
    path('dashboard/operative_input/', OperativeCreatePage.as_view(),  name= 'operative_create'),
    path('dashboard/record_details/<str:pk>/', RecordDetailPage.as_view(), name="record_detail"),

    path('dashboard/record_update/<str:pk>/', RecordUpdatePage.as_view(),  name= 'record_update'),
    path('dashboard/record_delete/<str:pk>', RecordDeletePage.as_view(),  name= 'record_delete'),

    path('dashboard/production_issue_update/', IssueFormPage.as_view(),  name= 'production_issue_update'),

    path('record_details/<str:pk>/<int:param>.pdf', Report.generate, name='run_pdfgen'),
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

