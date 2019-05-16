from django.urls import  path
from api import views

urlpatterns = [
    path('task_lists/', views.TaskLists.as_view()),
    path('task_lists/<int:pk>/', views.TaskListDetail.as_view()),
    path('task_lists/<int:pk>/tasks/', views.Tasks.as_view()),
    path('task_lists/<int:pk>/tasks/<int:pk2>/', views.TasksDetail.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('users/', views.UserList.as_view())
]