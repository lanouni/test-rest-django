from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

class TasksList(generics.ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerailizer
    