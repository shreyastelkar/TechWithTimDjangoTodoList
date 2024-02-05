from django.test import TestCase
from myapp.models import TodoItem, Item
# Create your tests here.

list1 = TodoItem(title="Shreyas's List", completed=False)

list1.save()

print(list1.id)

print(TodoItem.objects.all())


