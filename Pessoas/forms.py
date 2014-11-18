# coding: utf-8
from django import forms
from Pessoas.models import Pessoa

class cadastroForm(forms.Form):
	nickname = forms.CharField(max_length=100, required=True)
	nome = forms.CharField(max_length=100, required=True)
	sobrenome = forms.CharField(max_length=100, required=True)
	password = forms.CharField(widget=forms.PasswordInput, required=True)
	email = forms.CharField(max_length=100, required=True)