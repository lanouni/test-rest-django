from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', TasksList.as_view(),name = 'tasks-list'),
    #path('tasks/<int:pk>/', TasksDetail.as_view(),name = 'tasks-details')
    #path('subTasks/<int:subTask_id>/',SubTasks1ById.as_view(),name='subTask1-List-by-id')
]