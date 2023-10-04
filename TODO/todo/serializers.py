from rest_framework import serializers
from .models import TodoModel

class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ('taskname', 'created', 'updated', 'status', 'description', 'due_date')