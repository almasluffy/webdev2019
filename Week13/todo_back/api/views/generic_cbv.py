from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import authtoken



class TaskLists2(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer
    http_method_names = ['get']

class TaskLists(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # return TaskList.objects.all()
        return TaskList.objects.filter(created_by = self.request.user)

    def get_serializer_class(self):
        return TaskListSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

    def get_queryset(self):
        # return TaskList.objects.all()
        return TaskList.objects.for_user(self.request.user)


class TaskListTasks(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TaskList.objects.all()
    serializer_class = TaskSerializer

