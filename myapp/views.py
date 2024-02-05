from django.shortcuts import render, HttpResponse
from myapp.models import TodoItem, Item

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def index(response, name):
    ls = TodoItem.objects.get(title=name)
    ls.item_set.create(text="crazy")
    i = ls.id
    item = ls.item_set.get(id=i)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.title, str(item.text)))