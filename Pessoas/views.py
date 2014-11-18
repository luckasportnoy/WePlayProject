# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required
from Pessoas.models import Pessoa
from Pessoas.forms import cadastroPessoaForm, cadastroJogoForm, LoginForm

def index(request):
	return HttpResponse('Index')

def cadastro_Pessoa_validar(request):
	if request.method == 'POST':
		form = cadastroPessoaForm(request.POST)
		if form.is_valid():
			pessoa = Pessoa(
				username = form.data['nickname'],
				first_name = form.data['nome'],
				last_name = form.data['sobrenome'],
				email = form.data['email']
				#is_active=False
			)
		pessoa.set_password(form.data['senha'])
		pessoa.save()

		return render(request,'cadastro.html',{'form':form})

def cadastro_Jogo_validar(request):
	if request.method == 'POST':
		form = cadastroJogoForm(request.POST)
		if form.is_valid():
			jogo = Jogo(
				nome = form.data['nome'],
				genero = form.data['genero'],
				data_lancamento = form.data['data_lancamento'],
				imagem = form.data['imagem'],
			)
		jogo.save()

		return render(request,'cadastro.html',{'form':form})

def cadastro_pessoa(request):
	form = cadastroPessoaForm()
	return render(request,'cadastro.html',{'form':form})

def cadastro_jogo(request):
	form = cadastroJogoForm()
	return render(request,'cadastro.html',{'form':form})

def login(request):
	form = LoginForm()
	return render(request, 'login.html', {'form': form})

def logoff(request):
	logout(request)
	return HttpResponseRedirect('/')