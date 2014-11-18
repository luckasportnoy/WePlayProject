from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required

def index(request):
	return HttpResponse('Index')

def cadastro_validar(request):
	if request.method == 'POST':
		form = cadastroForm(request.POST)
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