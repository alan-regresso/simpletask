from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('nova/', views.criar_tarefa, name='criar_tarefa'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('excluir/<int:id>/', views.excluir_tarefa, name='excluir_tarefa'),
]
