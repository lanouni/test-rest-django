from django.urls import path
from .views import *

urlpatterns = [

    path('UserByTeam/<int:team_id>', PersonListByTeam.as_view(), name='Person-List-by-team'),
    path('TaskByPerson/<int:person_id>', TaskListByPerson.as_view(), name='task-List-by-team'),
    path('TrackTaskByPerson/<int:person_id>', TasksListWithTrackByPerson.as_view(), name='track-tasks-by-person'),

]
