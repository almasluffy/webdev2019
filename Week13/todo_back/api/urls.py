from django.urls import  path
from api import views

urlpatterns = [

    ##fbv
    # path('task_lists/', views.task_list),
    # path('task_lists/<int:pk>/', views.tasklist_detail),
    # path('task_lists/<int:pk>/tasks/', views.tasks),
    # path('task_lists/<int:pk>/tasks/<int:pk2>/', views.tasks_detail),

    ##cbv
    # path('task_lists/', views.TaskLists.as_view()),
    # path('task_lists/<int:pk>/', views.TaskListDetail.as_view()),
    # path('task_lists/<int:pk>/tasks/', views.Tasks.as_view()),
    # path('task_lists/<int:pk>/tasks/<int:pk2>/', views.Tasks_detail.as_view()),

    #generic
    path('task_lists/', views.TaskLists.as_view()),
    path('task_lists/<int:pk>/', views.TaskListDetail.as_view()),
    path('task_lists/<int:pk>/tasks/', views.Tasks.as_view()),
    path('task_lists/<int:pk>/tasks/<int:pk2>/', views.TasksDetail.as_view()),

    ##auth
    path('login/', views.login),
    path('logout/', views.logout),
    path('users/', views.UserList.as_view())
]