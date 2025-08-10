from django.shortcuts import render, get_object_or_404
from .models import Tarefa

# Create your views here.

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/listar_tarefas.html', {'tarefas': tarefas})

def detalhar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, 'tarefas/detalhar_tarefa.html', {'tarefas': tarefa})
