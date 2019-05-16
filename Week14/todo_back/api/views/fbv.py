from api.models import TaskList,Task
from api.serializers import TaskSerializer, TaskListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def tasklist_list(request):
    if request.method == 'GET':
        tasklists = TaskList.objects.all()
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
def tasklist_tasks(request, pk):
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

@api_view(['PUT','DELETE'])
def tasks(request,pk,pk2):
    try:
        taskInfo = TaskList.taskInfo_set.get(id = pk)
    except TaskList.DoesNotExist as e:
        return Response({'error',f'{e}'},status = status.HTTP_404_NOT_FOUND)


    if request.method == 'DELETE':
        task = taskInfo.task_set.get(id = pk2)
        task.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        task = taskInfo.task_set.get(id = pk2)
        serializer = TaskSerializer(instance=task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_500_INTERNAL_SERVER_ERROR)