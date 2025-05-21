from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("<int:id>", views.index, name="index"),
    path("form/", views.create, name="form"),
    
]

