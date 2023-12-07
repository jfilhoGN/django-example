from django.db import models

# Create your models here.
class Times(models.Model):
  nome_time = models.CharField(max_length=100)
  numero_integrantes = models.IntegerField(blank=True, null=True)
  inicio_projeto = models.TextField(max_length=100000)
  fim_projeto = models.CharField(max_length=100, null=True)
  
  def __str__(self):
    return self.nome_time
  