from django.contrib import admin
from .models import TodoItem, Item

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Item)  