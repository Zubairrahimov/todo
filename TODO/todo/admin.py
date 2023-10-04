from django.contrib import admin
from .models import TodoModel

@admin.register(TodoModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ('taskname', 'created', 'updated', 'status', )