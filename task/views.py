from django.shortcuts import render
from task.models import task

def all_tasks (request):
    all_tasks = task.objects.all()
    return render (request,'task/all_task.html',{'tasks':all_tasks})


def task_detail (request,task_id):
    pass


# Create your views here.
