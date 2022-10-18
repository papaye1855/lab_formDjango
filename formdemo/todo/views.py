from django.shortcuts import render , redirect
from django.core.files.storage import FileSystemStorage
from .models import Todo

from django.contrib import messages

# Create your views here.

def liste_des_todos(request):
    todos = Todo.objects.all()
    return render(request, "todo/todos.html",{"todos":todos})
def ajouter_un_todo(request):
    return render(request, "todo/ajouter-un-todo.html")
def valider_todo(request):
    if request.method == "GET":
        return redirect("todos:liste_des_todos")
    else:
        data = request.POST
        titre = data.get("todoNom")
        description = data.get("todoDesc")
        completedValue = data.get("todoComp")
        isCompleted = False
        if(completedValue == "oui"):
            isCompleted = True

        monFichier = request.FILES["todoImage"]
        fs = FileSystemStorage()
        nom_fichier = fs.save("static/images/todos/"+monFichier.name, monFichier)
        urlFichier = fs.url(nom_fichier)

        todo = Todo(img=nom_fichier,titre = titre,description = description,isCompleted = isCompleted)
        todo.save()

        messages.add_message(request, messages.SUCCESS, "Todo ajouté avec succès")

        return redirect("todos:liste_des_todos")
def todo_unique(request,id):
    todo = Todo.objects.get(pk=id)
    return render(request, "todo/todo-unique.html",{"todo":todo})
def modifier_todo(request):
    if request.method == "GET":
        return redirect("todos:liste_des_todos")
    else:
        data = request.POST
        todoId = data.get("todoId")
        titre = data.get("todoNom")
        description = data.get("todoDesc")
        completedValue = data.get("todoComp")
        isCompleted = False
        if(completedValue == "oui"):
            isCompleted = True

        todo = Todo.objects.get(pk=todoId)
        
        todo.titre =titre
        todo.description = description
        todo.isCompleted = isCompleted
        todo.save()

        return redirect("todos:liste_des_todos")
        







