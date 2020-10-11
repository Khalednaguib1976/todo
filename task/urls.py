from django.urls import path
from . import views


app_name = 'task'

urlpatterns = [
    path('',views.all_tasks),
    path('task_id',views.task_detail)
]
