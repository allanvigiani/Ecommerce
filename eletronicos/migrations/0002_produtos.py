from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('eletronicos', '0001_initial')
    ]

    operations = [
        migrations.RunSQL(
            sql="INSERT INTO eletronicos_produto(nome, descricao, preco, quantidade, avaliacao) VALUES('Mouse', 'Mouse otimo para games e afins', 10, 23, 5);INSERT INTO eletronicos_produto(nome, descricao, preco, quantidade, avaliacao) VALUES('Teclado', 'Teclado otimo para games e afins', 110, 2, 4);INSERT INTO eletronicos_produto(nome, descricao, preco, quantidade, avaliacao) VALUES('Headset', 'Headset otimo para games e afins', 76, 20, 2);INSERT INTO eletronicos_produto(nome, descricao, preco, quantidade, avaliacao) VALUES('Gabinete', 'Gabinete otimo para games e afins', 10, 23, 5);INSERT INTO eletronicos_produto(nome, descricao, preco, quantidade, avaliacao) VALUES('Web cam', 'Web cam otimo para games e afins', 22, 23, 5);INSERT INTO eletronicos_produto(nome, descricao, preco, quantidade, avaliacao) VALUES('Controle Xbox', 'Controle Xbox otimo para games e afins', 10, 23, 5);",
        )
    ]