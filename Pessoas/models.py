from django.db import models
from django.contrib.auth.models import AbstractUser

class Jogo(models.Model):
    nome = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    data_Lancamento = models.DateTimeField()
    imagem = models.ImageField(upload_to='GameImages')

class Pessoa(AbstractUser):
    games = models.ForeignKey(Jogo)
