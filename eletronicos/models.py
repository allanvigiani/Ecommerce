from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    dt_nascimento = models.DateField()
    estado = models.CharField(max_length=30)
    cidade  = models.CharField(max_length=60)
    encedereco = models.CharField(max_length=60)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.TextField(max_length=60, blank=True, null=True)
    preco = models.IntegerField()
    quantidade = models.IntegerField()
    avaliacao = models.IntegerField()
    
    def __str__(self):
        return self.nome

class Compra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.IntegerField()
    quantidade = models.IntegerField()
    dt_previsao = models.DateField()