from rest_framework import serializers
from .models import *
from  tasks.serializers import TasksSerailizer
from tasks.models import *
from rest_framework_simplejwt.tokens import RefreshToken


class PersonSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.name')
    team_name = serializers.CharField(source='team.name')
    class Meta :
        model = Person
        fields = ['id','lastName','name', 'email', 'gender', 'date_arrivee', 'date_depart', 'deleted',  'role_name','team_name']

class PersonsSerializer(serializers.ModelSerializer):
    tasks = TasksSerailizer(many=True, read_only= True)
    class Meta :
        model = Person
        fields = ['id', 'lastName', 'name', 'email', 'gender', 'date_arrivee', 'date_depart', 'deleted', 'role_name', 'team_name']


class TrackSerializer(serializers.ModelSerializer):
    task_name = serializers.CharField(source='task.task.name')
    class Meta :
        model = Track
        fields = ['id','nbrheures','date','task_name']


class TrackTest(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['date','nbrheures']
class TaskTest(serializers.ModelSerializer):
    track = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = ['id','name','track']

    def get_track(self, obj):
        person_id = self.context['person_id']

        sql = """SELECT tr.id, tr.nbrheures FROM tasks_tasks t , person_track tr, person_taskbyperson tp
                 WHERE t.id = tp.task_id AND tp.id = tr.task_id AND tp.task_id = %s AND tp.person_id = %s"""
        track = Track.objects.raw(sql,([obj.id,person_id]))
        serializer = TrackTest(track, many=True)
        return serializer.data


class TaskByPersonSerializer(serializers.ModelSerializer):
    task_name = serializers.CharField(source='task.name')
    task_id = serializers.CharField(source='task.id')
    task_description = serializers.CharField(source='task.description')
    task_startDate = serializers.CharField(source='task.startDate')
    task_endDate = serializers.CharField(source='task.endDate')
    task_commentaire = serializers.CharField(source='task.commentaire')
    task_sponsor = serializers.CharField(source='task.sponsor')
    task_chargeFTE = serializers.CharField(source='task.chargeFTE')
    task_statut = serializers.CharField(source='task.statut')
    task_type = serializers.CharField(source='task.type')

    class Meta:
        model = TaskByPerson
        fields = ['id','deleted','task_name','task_id','task_description','task_startDate','task_endDate','task_commentaire','task_sponsor','task_chargeFTE','task_statut','task_type']


class PersonLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=32)
    password = serializers.CharField(max_length=32)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        person = Person.objects.filter(email=email, password=password).first()
        if not person:
            raise serializers.ValidationError("Person not found")
        if person.deleted:
            raise serializers.ValidationError("Person is deleted")
        refresh = RefreshToken.for_user(person)
        token = str(refresh.access_token)
        attrs['token'] = token
        attrs['person'] = person
        print(attrs['token'])
        return attrs

