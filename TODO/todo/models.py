from django.db import models

# Create your models here.



class TodoModel(models.Model):
    taskname = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=False)
    description = models.CharField(max_length=10000)
    due_date = models.DateTimeField(null=True, blank=True)



    def __str__(self) -> str:
        return self.taskname