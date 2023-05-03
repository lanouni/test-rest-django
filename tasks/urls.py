from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', TasksList.as_view(),name = 'tasks-list'),
    #path('tasks/<int:pk>/', TasksDetail.as_view(),name = 'tasks-details')
    path('subTasks/<int:task_id>/',SubtaskList.as_view(),name='subTask1-List-by-id'),
    path('tasks/add', TasksCreateAPIView.as_view(), name='tasks-create'),
]