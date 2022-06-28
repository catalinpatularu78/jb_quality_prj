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
    path('dashboard/record_create/', RecordCreatePage.as_view(),  name= 'record_create'), # ensure this 
    path("dashboard/<str:pk>/", RecordDetailPage.as_view(), name="record_detail"),
    path('dashboard/<str:pk>/record_update/', RecordUpdatePage.as_view(),  name= 'record_update'),
    path('dashboard/<str:pk>/record_delete/', RecordDeletePage.as_view(),  name= 'record_delete'),


]