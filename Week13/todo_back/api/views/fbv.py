from api.models import TaskList,Task
from api.serializers import TaskSerializer, TaskListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
def task_list(request):
    if request.method == 'GET':
        tasklists = TaskList.objects.filter()
        serializer = TaskListSerializer(tasklists,many=True)
        return Response(serializer.data,status= status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','PUT','DELETE'])
def tasklist_detail(request,pk):
    try:
        tasklist = TaskList.objects.get(id = pk)
    except TaskList.DoesNotExist as e:
        return Response({'error',f'{e}'},status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskListSerializer(tasklist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer(instance=tasklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        tasklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def tasks(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({'error',f'{e}'},status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        task = tasklist.task_set.all()
        serializer = TaskSerializer(task,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def tasks_detail(request,pk,pk2):
    try:
        task = Task.objects.get(id=pk2)
    except Task.DoesNotExist as e:
        return Response({'error',f'{e}'},status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = TaskSerializer(instance=task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_500_INTERNAL_SERVER_ERROR)