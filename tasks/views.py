from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/listar_tarefas.html', {'tarefas': tarefas})

def detalhar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, 'tarefas/detalhar_tarefa.html', {'tarefas': tarefa})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/form_tarefa.html', {'form': form})

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/form_tarefa.html', {'form': form})

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect('listar_tarefas')

