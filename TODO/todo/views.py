from django.shortcuts import render , get_object_or_404
from .models import TodoModel
from .serializers import TodoModelSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta


# Create your views here.


class TodoListCreateView(APIView):
    def get(self, request, fromat = None):
        todos = TodoModel.objects.all()
        serializer = TodoModelSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, fromat = None):
        serializer = TodoModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(request.data, status.HTTP_400_BAD_REQUEST)
    

class TodoListDeleteView(APIView):
    def get(self, request, pk, fromat = None):
        todo = get_object_or_404(TodoModel, pk=pk)
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)
    
    def patch(self, request, pk, fromat = None):
        todo = get_object_or_404(TodoModel, pk=pk)
        serializer = TodoModelSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, fromat = None):
        todo = get_object_or_404(TodoModel , pk=pk)
        todo.delete()
        return Response({'message' : 'Task deleted successfully'})
    

class TodoTodayListView(APIView):
    def get(self, request, fromat = None):
        today = timezone.now().date()
        todos = TodoModel.objects.filter(created__date=today)
        serializer = TodoModelSerializer(todos , many=True)
        return Response(serializer.data)
    

class TodoLast10daysListView(APIView):
    def get(self, request, format = None):
        ten_days_ago = timezone.now() - timedelta(days=10)
        todos = TodoModel.objects.filter(created__date=ten_days_ago.date())
        serializer = TodoModelSerializer(todos , many=True)
        return Response(serializer.data)
    

class TodoDoneListView(APIView):
    def get(self, request, format=None):
        todos = TodoModel.objects.filter(status=True)
        serializer = TodoModelSerializer(todos, many=True)
        return Response(serializer.data)
    

