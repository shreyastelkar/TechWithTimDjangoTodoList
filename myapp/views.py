from django.shortcuts import render, HttpResponse
from .models import TodoItem, Item

# Create your views here.
def home(request):
    return render(request, "base.html", {"name": "test"})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def index(response, id):
    ls = TodoItem.objects.get(id=id)
    return render(response, "home.html", {"ls":ls})

def create(response):
    pass