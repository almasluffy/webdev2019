from api.models import TaskList,Task
from api.serializers import TaskListSerializer,TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class TaskLists(APIView):
    def get(self,request):
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer(tasklists,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def post(self,request):
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_500_INTERNAL_SERVER_ERROR)



class TaskListDetail(APIView):

    def get_object(self,pk):
        try:
            return TaskList.objects.get(id = pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        tasklist = self.get_object(pk)
        serializer = TaskListSerializer(tasklist)
        return Response(serializer.data)

    def put(self,request,pk):
        tasklist = self.get_object(pk)
        serializer = TaskListSerializer(instance=tasklist,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,pk):
        tasklist = self.get_object(pk)
        tasklist.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class Tasks(APIView):
    def get_object(self,pk):
        try:
            return TaskList.objects.get(id = pk)
        except TaskList.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        taskslist = self.get_object(pk)
        tasks = taskslist.task_set.all()
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self,request,pk):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class Tasks_detail(APIView):
    def get_object(self,pk):
        try:
            return Task.objects.get(id = pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, pk2):
        task = self.get_object(pk2)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self,request,pk,pk2):
        task = self.get_object(pk2)
        serializer = TaskSerializer(instance=task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self,request,pk,pk2):
        task = self.get_object(pk2)
        task.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)
