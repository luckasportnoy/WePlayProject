from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    password = models.CharField(max_length=18)
    
class Jogo(models.Model):
    nome = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    data_lancamento = models.DateTimeField()
    imagem = models.ImageField(upload_to='GameImages')