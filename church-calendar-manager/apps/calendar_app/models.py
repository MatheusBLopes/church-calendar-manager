from django.contrib.auth.models import User
from django.db import models


class Ministerio(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    ministerio = models.ForeignKey(Ministerio, on_delete=models.CASCADE)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    ocorreu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} - {self.data}"

class ConflitoMarcado(models.Model):
    evento1 = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="conflito_1")
    evento2 = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="conflito_2")
    justificativa = models.TextField()
