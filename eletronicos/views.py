from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cliente
from django.urls import reverse_lazy
import psycopg2
from datetime import date

# Create your views here.
def home(request):

    produtos = {}

    conn = db_connect()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM eletronicos_produto;")

    produtos['produto'] = cursor.fetchall()

    return render(request, 'home/index.html', context=produtos)

def atendimento(request):
    return render(request, 'atendimento/index.html')

def carrinho(request):
    return render(request, 'carrinho/index.html')

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
        password = request.POST.get('password', None)
        
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

        if password == '':
            error['password'] = 'O campo Senha nao pode ser vazio'

        if error:
            context['error'] = error
        else:
            conn = db_connect()
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO eletronicos_cliente (nome, email, cpf, dt_nascimento, uf, cidade, endereco, login, senha) VALUES('{nome}', '{email}', '{cpf}', '{dt_nascimento}', '{uf}', '{cidade}', '{endereco}', '{login}', '{password}');")
            
            cursor.execute("SELECT * FROM eletronicos_cliente ORDER BY id DESC LIMIT 1")
            for cliente in cursor:
                id_cliente = cliente[0]
            
            cursor.execute(f"INSERT INTO eletronicos_usuario (tipo, dt_cadastro, administrativo, cliente_id) VALUES(1, '{date.today()}', 'f', {id_cliente});")
            conn.commit()
            context['sucesso'] = 'Cadastro realizado com sucesso.'

    return render(request, 'cadastro/index.html', context=context)

def login(request):

    context = {}

    if request.method == 'POST':
        
        error = {}

        login = request.POST.get('login', None)
        password = request.POST.get('password', None)

        if login == '':
            error['login'] = 'O campo Login nao pode ser vazio'

        if password == '':
            error['password'] = 'O campo Senha nao pode ser vazio'

        if error:
            context['error'] = error
        else:
            conn = db_connect()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM eletronicos_cliente;")
            for clientes in cursor:
                print(clientes)
                if login == clientes[8] and password == clientes[9]:
                    context['message'] = 'Usuario logado.'
                    break
                else:
                    context['message'] = 'Usuario ou Senha incorretos.'

            

    return render(request, 'login/index.html', context=context)


def db_connect():
    conn = psycopg2.connect("dbname=ecommerce user=postgres")
    return conn