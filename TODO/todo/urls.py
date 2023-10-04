from django.urls import path
from .views import (
    TodoListCreateView,
    TodoListDeleteView,
    TodoTodayListView,
    TodoLast10daysListView,
    TodoDoneListView
    
)

urlpatterns =[

    path('todolist/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoListDeleteView.as_view()),
    path('todos/today/', TodoTodayListView.as_view(), name='todo-today-list'),
    path('todos/last-10-days/', TodoLast10daysListView.as_view(), name='todo-last-10-days-list'),
    path('todos/done/', TodoDoneListView.as_view(), name='todo-done-list')
]
