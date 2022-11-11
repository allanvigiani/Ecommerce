from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cliente
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def cadastro(request):

    context = {}

    if request.method == 'POST':

        error = {}

        nome = request.POST.get('nome', None)
        email = request.POST.get('email', None)
        cpf = request.POST.get('cpf', None)
        dt_nascimento = request.POST.get('dt_nascimento', None)
        uf = request.POST.get('uf', None)
        cidade = request.POST.get('cidade', None)
        endereco = request.POST.get('endereco', None)
        login = request.POST.get('login', None)
        senha = request.POST.get('senha', None)
        
        if nome == '':
            error['nome'] = 'O campo Nome nao pode ser vazio'

        if email == '':
            error['email'] = 'O campo Email nao pode ser vazio'

        if cpf == '':
            error['cpf'] = 'O campo CPF nao pode ser vazio'

        if dt_nascimento == '':
            error['dt_nascimento'] = 'O campo Data de Nascimento nao pode ser vazio'

        if cidade == '':
            error['cidade'] = 'O campo Cidade nao pode ser vazio'

        if endereco == '':
            error['endereco'] = 'O campo Endereco nao pode ser vazio'

        if login == '':
            error['login'] = 'O campo Login nao pode ser vazio'

        if senha == '':
            error['senha'] = 'O campo Senha nao pode ser vazio'

        if error:
            context['error'] = error
        else:
            print('SALVA OS DADOS')
            context['sucesso'] = 'Cadastro realizado com sucesso.'

    return render(request, 'cadastro/index.html', context=context)

def login(request):
    return render(request, 'login/index.html')

class ClienteCreate(CreateView):
    pass