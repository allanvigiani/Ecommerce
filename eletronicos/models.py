from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=30, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    cpf = models.CharField(max_length=11,verbose_name="CPF")
    dt_nascimento = models.DateField(verbose_name="Data de Nascimento")
    uf = models.CharField(max_length=2, verbose_name="UF")
    cidade  = models.CharField(max_length=60, verbose_name="Cidade")
    endereco = models.CharField(max_length=60, verbose_name="Endereco")
    login = models.CharField(max_length=20, verbose_name="Login")
    senha = models.CharField(max_length=200, verbose_name="Senha")

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    tipo = models.IntegerField()
    dt_cadastro = models.DateField()
    administrativo = models.BooleanField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Produto(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.TextField(max_length=60, blank=True, null=True)
    preco = models.FloatField()
    quantidade = models.IntegerField()
    avaliacao = models.IntegerField()
    imagem = models.TextField()
    
    def __str__(self):
        return self.nome

class Compra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.IntegerField()
    quantidade = models.IntegerField()
    dt_previsao = models.DateField()