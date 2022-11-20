# Generated by Django 4.1.3 on 2022-11-20 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('dt_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('cidade', models.CharField(max_length=60, verbose_name='Cidade')),
                ('endereco', models.CharField(max_length=60, verbose_name='Endereco')),
                ('login', models.CharField(max_length=20, verbose_name='Login')),
                ('senha', models.CharField(max_length=200, verbose_name='Senha')),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('descricao', models.TextField(blank=True, max_length=60, null=True)),
                ('preco', models.FloatField()),
                ('quantidade', models.IntegerField()),
                ('avaliacao', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField()),
                ('dt_cadastro', models.DateField()),
                ('administrativo', models.BooleanField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eletronicos.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('quantidade', models.IntegerField()),
                ('dt_previsao', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eletronicos.cliente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eletronicos.produto')),
            ],
        ),
    ]
