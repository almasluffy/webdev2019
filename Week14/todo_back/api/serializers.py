from rest_framework import serializers

from api.models import TaskList, Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        # fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):

    task_list_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'name', 'complexity', 'status', 'task_list_id')
class TaskSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'name', 'complexity', 'status')

class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)
    # tasks = serializers.StringRelatedField(many=True)
    # tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tasks = TaskSerializer2(many=True, required=False)
    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by', 'tasks')
    def create(self, validated_data):
        tasks = validated_data.pop('tasks')
        task_list = TaskList.objects.create(**validated_data)
        for task in tasks:
            Task.objects.create(task_list=task_list, **task)
        return task_list

    # def create(self, validated_data):
    #     task_list = TaskList(**validated_data)
    #     task_list.save()
    #     return task_list
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance



