from django.db import models

class ONGModel(models.Model):
  Nome = models.CharField('Nome', max_length=50, default='')
  Telefone = models.CharField('Telefone', max_length=15, default='')
  Email = models.EmailField('Email', max_length=50, default='')
  Descricao = models.TextField('Descriacao', default='')
  Senha = models.CharField('Senha', max_length=128, default='')
  CNPJ = models.CharField('CNPJ', max_length=15, default='', primary_key=True)
  
  def __str__(self):
    return self.nome