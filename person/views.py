from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
from tasks.models import *
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class PersonListByTeam(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        sql = """SELECT p.id,p.name, p.email, p.gender, p.date_arrivee, p.date_depart, p.deleted, r.name as role_name, t.name as team_name 
                 FROM person_person p , role_role r , teams_teams t WHERE p.role_id = r.id AND t.id = p.team_id AND t.id = %s"""
        qs = Person.objects.raw(sql, ([team_id]))
        return qs

class TaskListByPerson(generics.ListAPIView):
    serializer_class = TaskByPersonSerializer
    def get_queryset(self):
        person_id = self.kwargs['person_id']
        sql = """SELECT t.id, t.name, t.description FROM tasks_tasks t , person_taskbyperson tp WHERE t.id = tp.task_id AND tp.person_id = %s  """
        qs = TaskByPerson.objects.raw(sql,([person_id]))
        return qs


class TrackTaskByID(generics.ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        sql = """"""
        qs = Track.objects.raw(sql,([task_id]))
        return qs

class TrackTasksByPerson(generics.ListAPIView):
     serializer_class = TrackSerializer

     def get_queryset(self):
         person_id = self.kwargs['person_id']
         sql = """SELECT tr.id, t.name, tr.nbrheures , tr.date FROM tasks_tasks t , person_track tr, person_taskbyperson tp
                 WHERE t.id = tp.task_id AND tp.id = tr.task_id AND tp.person_id = %s
                  """
         qs = Track.objects.raw(sql, ([person_id]))
         return qs

class TasksListWithTrackByPerson(generics.ListAPIView):
    serializer_class =TaskTest

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['person_id'] = self.kwargs['person_id']
        return context

    def get_queryset(self):
        person_id = self.kwargs['person_id']
        sql = """SELECT t.id, t.name FROM person_taskbyperson tp, tasks_tasks t
            WHERE t.id = tp.task_id AND tp.person_id = %s"""
        qs = Tasks.objects.raw(sql,([person_id]))
        return  qs

    #def get_serializer(self, *args, **kwargs):
    #    kwargs['person_id'] = int(self.kwargs['person_id'])
    #    return super().get_serializer(*args, **kwargs)

class PersonLoginView(APIView):
    serializer_class = PersonLoginSerializer
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        serializer = PersonLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)