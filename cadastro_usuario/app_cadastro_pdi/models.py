from django.db import models

# Create your models here.
class CadastroPdi(models.Model):
    nome = models.CharField(max_length=20)
    idade = models.IntegerField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome