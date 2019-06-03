from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import authtoken


from django.http import Http404

from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination





class TaskLists(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.filter(created_by = self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    # queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return TaskList.objects.filter(created_by=self.request.user)



class Tasks(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = TaskSerializer

    def get_queryset(self):
        tasklist = TaskList.objects.filter(created_by=self.request.user.id).get(id=self.kwargs['pk'])
        queryset = tasklist.task_set.all()
        return queryset

class TasksDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    # def get_queryset(self):
    #     return Task.objects.filter(id=self.kwargs['pk2'])
    #
    # def get_serializer_class(self):
    #     return TaskSerializer

    serializer_class = TaskSerializer
    lookup_url_kwarg = "pk2"

    def get_queryset(self):
        try:
            task_list = TaskList.objects.get(id=self.kwargs.get('pk'))
        except TaskList.DoesNotExist:
            raise Http404
        queryset = task_list.task_set.filter(id=self.kwargs.get('pk2'))
        return queryset

