from django.shortcuts import render, redirect, get_object_or_404
from .models import Task 
from .forms import TaskForm

def lista_tarefas(request):
    tarefas = Task.objects.all()
    return render(request, 'tasks/list.html', {'tarefas': tarefas})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('lista_tarefas')
    else:
        form = TaskForm()
    return render(request, 'tasks/form.html', {'form': form})

def editar_tarefa(request, id):
    tarefa = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()  
            return redirect('lista_tarefas')
    else:
        form = TaskForm(instance=tarefa)
    return render(request, 'tasks/form.html', {'form': form})

def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        tarefa.delete()  
        return redirect('lista_tarefas')
    return render(request, 'tasks/list.html', {'tarefa': tarefa})