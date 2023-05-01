from django.urls import path
from .views import *

urlpatterns = [
    path('teams/', TeamsList.as_view(),name = 'tasks-list'),
    #path('teams/<int:pk>/', TeamsDetails.as_view(),name = 'tasks-details'),
    ##path('TeamsTasks/', TeamsTasksList.as_view(), name='teams-tasks-list'),
    path('TeamsTasks/<int:team_id>', TaskListBy.as_view(), name='teams-tasks-details'),
    ##path('TeamsTasksbyTeam/<int:team_id>', TeamTasksByTeamID.as_view(), name='teams-tasks-Id'),
    #path('TeamTasksList/<int:team_id>', TeamTasksList.as_view(), name='Team-Tasks-List-details')

]