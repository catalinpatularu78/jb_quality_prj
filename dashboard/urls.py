# dashboard URL file 
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path , include
from django.contrib.auth.views import LogoutView

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
    path("dashboard/record_details/<uuid:pk>/", RecordDetailPage.as_view(), name="record_detail"),
    path('dashboard/record_update/<uuid:pk>/', RecordUpdatePage.as_view(),  name= 'record_update'),
    path('dashboard/record_delete/<uuid:pk>', RecordDeletePage.as_view(),  name= 'record_delete'),

    path('dashboard/production_issue_update/', IssueFormPage.as_view(),  name= 'production_issue_update'),
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)