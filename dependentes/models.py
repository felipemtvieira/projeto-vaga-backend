from django.db import models
from colaboradores.models import Colaborador

class Dependente(models.Model):
    nome = models.CharField(max_length=100)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
