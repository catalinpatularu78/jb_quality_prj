# dashboard URL file 

from django.urls import path

from .views import (
    HomePage,
    DashboardPage,
    RecordDetailPage,
    RecordCreatePage,
    RecordUpdatePage,
    RecordDeletePage,

)

urlpatterns = [
    
    path('', HomePage.as_view(),  name= 'main_page'),
    path('dashboard/', DashboardPage.as_view(),  name= 'dashboard'),
    path('dashboard/record_create/', RecordCreatePage.as_view(),  name= 'record_create'),
    path("dashboard/record_details/<str:pk>/", RecordDetailPage.as_view(), name="record_detail"),
    path('dashboard/record_update/<str:pk>/', RecordUpdatePage.as_view(),  name= 'record_update'),
    path('dashboard//record_delete/<str:pk>', RecordDeletePage.as_view(),  name= 'record_delete'),


]