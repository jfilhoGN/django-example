from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    data_nascimento = models.DateField(blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome