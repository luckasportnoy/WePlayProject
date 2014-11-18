# coding: utf-8
from django import forms
from Pessoas.models import Pessoa

class cadastroPessoaForm(forms.Form):
	nickname = forms.CharField(max_length=100, required=True)
	nome = forms.CharField(max_length=100, required=True)
	sobrenome = forms.CharField(max_length=100, required=True)
	email = forms.CharField(max_length=100, required=True)
	senha = forms.CharField(widget=forms.PasswordInput, required=True)

class cadastroJogoForm(forms.Form):
    nome = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    data_lancamento = models.DateTimeField()
    imagem = models.ImageField(upload_to='GameImages')

class LoginForm(forms.Form):
	login = forms.CharField(max_length=100, required=True)
	senha = forms.CharField(widget=forms.PasswordInput, required=True)