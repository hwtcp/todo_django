"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import listar_tarefas, detalhar_tarefa, criar_tarefa, editar_tarefa, excluir_tarefa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_tarefas, name='listar_tarefas'),  # página inicial lista tarefas
    path('<int:pk>/detalhar_tarefa/', detalhar_tarefa, name='detalhar_tarefa'),
    path('criar_tarefa/', criar_tarefa, name='criar_tarefa'),
    path('<int:pk>/editar_tarefa/', editar_tarefa, name='editar_tarefa'),
    path('<int:pk>/excluir_tarefa/', excluir_tarefa, name='excluir_tarefa'),
]


