from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import TodoItem, Item
from .forms import CreaNewList

# Create your views here.
def home(request):
    return render(request, "base.html", {"greeting": "Welcome Shreyas"})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def index(response, id):
    ls = TodoItem.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                
                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get('new')
            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print('invalid')

    return render(response, "home.html", {"ls":ls})

def create(response):
    if response.method == 'POST':
        form = CreaNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = TodoItem(title=str(n), completed=False)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreaNewList()
    return render(response, "form.html", {"form":form})
