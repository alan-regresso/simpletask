from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Project
from .forms import TaskForm, ProjectForm

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

projetos = Project.objects.all()
return render(request, 'tasks/form.html', {'form': form, 'projetos': projetos})

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

def lista_projetos(request):
projetos = Project.objects.all()
return render(request, 'projects/list.html', {'projetos': projetos})

def criar_projeto(request):
if request.method == 'POST':
form = ProjectForm(request.POST)
if form.is_valid():
form.save()
return redirect('lista_projetos')
else:
form = ProjectForm()
return render(request, 'projects/form.html', {'form': form})
