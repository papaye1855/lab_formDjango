
from django.contrib import admin
from django.urls import path , include

from .views import *

app_name="todos"

urlpatterns = [
    path("",liste_des_todos,name="liste_des_todos"),
    path("ajouter-un-todo/",ajouter_un_todo,name="ajouter_un_todo"),
    path("valider-todo/",valider_todo, name="valider_todo"),
    path("<int:id>/", todo_unique , name="todo_unique"),
    path("modifier-todo/",modifier_todo, name="modifier_todo")
]
