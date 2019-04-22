from django.urls import  path
from api import views

urlpatterns = [
    path('task_lists/', views.show_task_list),
    path('task_lists/<int:pk>/', views.tasklist_detail),
    path('task_lists/<int:pk>/tasks/', views.show_tasks),
    path('task_lists/<int:pk>/tasks/<int:pk2>/', views.show_tasks_detail)
]