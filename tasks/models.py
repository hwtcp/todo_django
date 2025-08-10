from django.db import models

# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
    feito = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
