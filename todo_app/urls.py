from django.urls import path
from . import views

urlpatterns = [
    path('lists/', views.task_list_collection, name='task_list_collection'),
    path('lists/<int:list_id>/', views.task_list_detail, name='task_list_detail'),
    path('lists/<int:list_id>/tasks/', views.task_collection, name='task_collection'),
    path('lists/<int:list_id>/tasks/<int:task_id>/', views.task_detail, name='task_detail'),
]
