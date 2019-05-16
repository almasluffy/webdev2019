from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import authtoken
from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from api.filters import TaskFilter
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class TaskLists2(generics.ListAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    http_method_names = ['get']

class TaskLists(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer


    def get_queryset(self):
        # return TaskList.objects.all()
        return TaskList.objects.filter(created_by=self.request.user)


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    # queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return TaskList.objects.filter(created_by=self.request.user)


class Tasks(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # TODO DjangoFilterBackend
    # filterset_fields = ('name', 'price',)
    filter_class = TaskFilter

    # TODO SearchFilter
    search_fields = ('name', 'complexity', 'status')

    # TODO OrderingFilter
    ordering_fields = ('name', 'complexity')
    ordering = ('complexity',)


    def get_queryset(self):
        task_list = get_object_or_404(TaskList, id=self.kwargs.get('pk'))
        queryset = task_list.tasks.all()
        return queryset

class TasksDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        task = get_object_or_404(Task, id=self.kwargs.get('pk2'))
        return task
        # task_list = get_object_or_404(TaskList, id=self.kwargs.get('pk'))
        # my_tasks = task_list.tasks.all()
        # task = get_object_or_404(Task, id=my_tasks.kwargs.get('pk2'))
        # return task
