from django.shortcuts import render, redirect
from .models import Todos
# Create your views here.
def home(request):
    if request.method == "POST" :
        todo = Todos(title=request.POST["title"], description = request.POST["description"])
        todo.save()
        return redirect("todo-home")
    return render(request,"todos/index.html",{"Todos":Todos.objects.all()})
    
def delete(request,pk):
    item_to_delete = Todos.objects.filter(id=pk)
    item_to_delete.delete()
    return redirect("todo-home")