from django.urls import  path
from api import views

urlpatterns = [
    path('task_lists/', views.show_lists),
    path('task_lists/<int:pk>/', views.show_list),
    path('task_lists/<int:pk>/tasks/', views.show_task)
]