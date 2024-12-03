from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/add_task/', views.add_task, name='add_task'),
    path('admin/view_submissions/', views.view_submissions, name='view_submissions'),

    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('points/', views.view_points, name='view_points'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    path('submit_task/<int:task_id>/', views.submit_task, name='submit_task'),

    path('', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
] 