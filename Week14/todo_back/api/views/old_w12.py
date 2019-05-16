from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from api.models import TaskList,Task
from django.views.decorators.csrf import csrf_exempt
from api.serializers import TaskListSerializer, TaskSerializer

@csrf_exempt
def show_task_list(request):

    if request.method == "GET":
        task_list = TaskList.objects.all()
        serializer = TaskListSerializer(task_list, many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)


@csrf_exempt
def tasklist_detail(request, pk):
    try:
        tasks = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})


    if request.method == "GET":
        serializer = TaskListSerializer(tasks)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = TaskListSerializer(instance=tasks, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    elif request.method == "DELETE":
        tasks.delete()
        return JsonResponse({})

@csrf_exempt
def show_tasks(request,pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    if request.method == "GET":
        tasks = task_list.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

@csrf_exempt
def show_tasks_detail(request, pk, pk2):
    try:
        my_task = Task.objects.get(id=pk2)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == "GET":
        serializer = TaskSerializer(my_task)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = TaskSerializer(instance=my_task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    elif request.method == "DELETE":
        my_task.delete()
        return JsonResponse({})