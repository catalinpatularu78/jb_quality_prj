from django.urls import path
from . import views

urlpatterns = [
    path('api/dashboard/', views.dashboard_model_list, name='dashboard-list'),
]
