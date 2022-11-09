from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cliente
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'login/index.html')

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'email', 'cpf', 'dt_nascimento', 'uf', 'cidade', 'endereco', 'login', 'senha']
    template_name = 'login/index.html'
    success_url = reverse_lazy('home')
