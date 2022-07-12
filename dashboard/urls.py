# dashboard URL file 

from django.urls import path

from .views import (
    HomePage,
    DashboardPage,
    RecordDetailPage,
    RecordCreatePage,
    RecordUpdatePage,
    RecordDeletePage,
    IssueFormPage,
)

urlpatterns = [
    
    path('', HomePage.as_view(),  name= 'main_page'),
    path('dashboard/', DashboardPage.as_view(),  name= 'dashboard'),
    path('dashboard/record_create/', RecordCreatePage.as_view(),  name= 'record_create'),
    path("dashboard/record_details/<uuid:pk>/", RecordDetailPage.as_view(), name="record_detail"),
    path('dashboard/record_update/<uuid:pk>/', RecordUpdatePage.as_view(),  name= 'record_update'),
    path('dashboard/record_delete/<uuid:pk>', RecordDeletePage.as_view(),  name= 'record_delete'),

    path('dashboard/production_issue_update/', IssueFormPage.as_view(),  name= 'production_issue_update'),
]