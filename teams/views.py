from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Teams
from .serializers import *
from django.db import connection
from tasks.serializers import TasksSerailizer
from tasks.models import Tasks



# Create your views here.

class TeamsList(generics.ListCreateAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

class TaskListBy(generics.ListAPIView):
    serializer_class = TaskByTeamSerializer

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        sql = """SELECT t.id,t.name,t.description,t.startdate, t.enddate , t.commentaire , t.sponsor, t.chargeFTE , t.deleted , 
        t.statut FORM FROM person_taskbyperson tp, tasks_tasks t, person_person p
            WHERE t.id = tp.task_id AND tp.person_id = p.id AND p.team_id = %s"""
        queryset = Tasks.objects.raw(sql,([team_id]))
        return queryset
