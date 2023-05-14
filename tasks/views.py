from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.

class TasksList(generics.ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerailizer
    
class SubtaskList(generics.ListAPIView):
    serializer_class = TasksTestSerailizer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['task_id'] = self.kwargs['task_id']
        return context
    
    def get_queryset(self):
        task_id = self.kwargs['task_id']
        
        qs = Tasks.objects.filter(task_id=task_id)
        return qs
    
class TasksCreateAPIView(generics.CreateAPIView):
    serializer_class = TasksSerailizer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@require_GET
def tasks_with_subtasks(request):
    sql = """SELECT t.id,t.name,t.description,t.startdate, t.enddate , t.commentaire , t.sponsor, t.chargeFTE , t.deleted , 
        t.statut FORM FROM person_taskbyperson tp, tasks_tasks t, person_person p
            WHERE t.id = tp.task_id AND tp.person_id = p.id AND p.team_id = %s"""
    tasksTeam = Tasks.objects.raw(sql,([1]))
    tasks = Tasks.objects.all()
    result = []
    for task in tasks:
        subtask1_list = []
        if task.id == tasksTeam.id:
            subtasks1 = Tasks.objects.filter(task_id=task.id)
            
   