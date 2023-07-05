from django.shortcuts import render
from .models import Utilizador

def home(request):
    return render(request, 'usuarios/home.html')
def usuarios(request):
    novo_usuario = Utilizador()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #exibir os usuarios cadastrados em uma nova janela , 
    usuarios = {
        'usuarios': Utilizador.objects.all()
    }
    #retornar os dados para a pagina
    return render(request,'usuarios/usuarios.html', usuarios)

def cadastro(request):
    cadastro = {
        'cadastro': Utilizador.objects.all()
    }
    #retornar os dados para a pagina
    return render(request,'usuarios/lista_cadastro.html', cadastro)