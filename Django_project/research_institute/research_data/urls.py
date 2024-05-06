from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('projects/', views.project_list, name='project_list'),
    path('employee/new/', views.employee_new, name='employee_new'),
    path('project/new/', views.project_new, name='project_new'),
    path('employee/<int:id>/edit/', views.employee_edit, name='employee_edit'),
    path('project/<int:id>/edit/', views.project_edit, name='project_edit'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('', views.home, name='home')
]

