from rest_framework import serializers
from .models import Tasks

class TasksSerailizer(serializers.ModelSerializer):
    class Meta :
        model = Tasks
        fields = "__all__"

class TasksTestSerailizer(serializers.ModelSerializer):
    subtask = serializers.SerializerMethodField()
    class Meta :
        model = Tasks
        fields = "__all__"

    def get_subtask(self, obj):
        subtask = Tasks.objects.filter(task_id=obj.id)
        serializer = SubTasksSerailizer(subtask, many=True)
        return serializer.data
        

class SubTasksSerailizer(serializers.ModelSerializer):
    class Meta :
        model = Tasks
        fields = "__all__"