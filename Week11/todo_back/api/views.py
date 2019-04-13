from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import TaskList,Task

def show_lists(request):
    tasks = TaskList.objects.all()
    json_tasks = [c.to_json() for c in tasks]
    return  JsonResponse(json_tasks, safe=False)

def show_list(request,pk):
    try:
        tasks = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)

    return JsonResponse(tasks.to_json())

def show_task(request,pk):
    try:
        t_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)

    my = t_list.task_set.all()
    json_my = [p.to_json() for p in my]

    return JsonResponse(json_my, safe=False)