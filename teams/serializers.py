from rest_framework import serializers
from .models import Teams
from tasks.models import *

class TeamsSerializer(serializers.ModelSerializer):
    class Meta :
        model = Teams
        fields = ['id', 'name','Fullname','deleted']



class TaskByTeamSerializer(serializers.ModelSerializer):


    class Meta:
        model = Tasks
        fields = ['id', 'name','description', 'startdate', 'enddate','commentaire', 'sponsor', 'chargefte', 'deleted', 'statut','type']