from rest_framework import serializers

from api.models import TaskList, Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        # fields = '__all__'

class TaskListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_by = UserSerializer(read_only=True)

    def create(self, validated_data):
        task_list = TaskList(**validated_data)
        task_list.save()
        return task_list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=False)
    due_on = serializers.DateTimeField(required=False)
    status = serializers.CharField(required=False)

    class Meta:
        model = Task
        fields = ('id', 'name', 'created_at', 'due_on', 'status', 'task_list')
#
#
# class TasksSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#
#     # task_list = TaskListSerializer(read_only=True)
#
#     class Meta:
#         model = Task
#         fields = ('id', 'name', 'created_at', 'due_on', 'status', 'task_list')
#
#     def create(self, data):
#         t = data.pop('task_list')
#         return Task.objects.create(task_list=t, **data)
#
#     def update(self, instance, data):
#         instance.name = data.get('name', instance.name)
#         instance.created_at = data.get('created_at', instance.created_at)
#         instance.due_on = data.get('due_on', instance.due_on)
#         instance.status = data.get('status', instance.status)
#         instance.task_list = data.get('task_list', instance.task_list)
#         instance.save()
#         return instance
