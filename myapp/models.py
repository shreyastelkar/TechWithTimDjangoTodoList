from django.db import models

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
    def __bool__(self) -> str:
        return self.completed

class Item(models.Model):
    todolist = models.ForeignKey(TodoItem, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.text