# coding: utf-8
from django import forms
from Pessoas.models import Pessoa, Jogo

class cadastroPessoaForm(forms.Form):
	nickname = forms.CharField(max_length=100, required=True)
	nome = forms.CharField(max_length=100, required=True)
	sobrenome = forms.CharField(max_length=100, required=True)
	email = forms.CharField(max_length=100, required=True)
	senha = forms.CharField(widget=forms.PasswordInput, required=True)

class cadastroJogoForm(forms.ModelForm):
	class Meta:
		model = Jogo

class LoginForm(forms.Form):
	login = forms.CharField(max_length=100, required=True)
	senha = forms.CharField(widget=forms.PasswordInput, required=True)