from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_service_request, name='submit_request'),
    path('status/<int:request_id>/', views.request_status, name='request_status'),
    path('requests/', views.request_list, name='request_list'),
    path('support/', views.support_dashboard, name='support_dashboard'),
    path('update/<int:request_id>/', views.update_request_status, name='update_request_status'),
]
