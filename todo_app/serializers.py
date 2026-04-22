from rest_framework import serializers
from .models import TaskList, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'created_at', 'task_list']
        read_only_fields = ['id', 'created_at']

class TaskListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = TaskList
        fields = ['id', 'name', 'created_at', 'tasks']
        read_only_fields = ['id', 'created_at']
