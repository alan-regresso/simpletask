from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'registration/login.html', {'erro': True})
    return render(request, 'registration/login.html')


@login_required
def dashboard(request):
    return render(request, 'tasks/dashboard.html')


@login_required
def task_list(request):
    return render(request, 'tasks/task_list.html')

@login_required
def task_create(request):
    return render(request, 'tasks/form.html')

@login_required
def task_complete(request, pk): 
    return redirect('dashboard')

@login_required
def task_delete(request, pk):
    return redirect('dashboard')

@login_required
def task_update_status(request, pk):
    return redirect('dashboard')


@login_required
def project_list(request):
    return render(request, 'projects/list.html')

@login_required
def project_create(request):
    return render(request, 'projects/form.html')

@login_required
def project_update(request, pk):
    return render(request, 'projects/form.html')

@login_required
def project_delete(request, pk):
    return redirect('project_list')