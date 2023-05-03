from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response

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