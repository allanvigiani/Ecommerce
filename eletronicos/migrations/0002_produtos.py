from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('eletronicos', '0001_initial')
    ]

    operations = [
        migrations.RunSQL(
            sql="INSERT INTO eletronicos_produto(nome, descricao, preco, quantidade, avaliacao, imagem) VALUES('Mouse', 'Mouse otimo para games e afins', 10, 23, 5, 'https://images.kabum.com.br/produtos/fotos/165921/mouse-gamer-corsair-sabre-rgb-pro-champion-series-8-botoes-18000dpi-preto-ch-9303111-na_1636487831_g.jpg');INSERT INTO eletronicos_produto(nome, descricao, preco, quantidade, avaliacao, imagem) VALUES('Teclado', 'Teclado otimo para games e afins', 110, 2, 4, 'https://images.tcdn.com.br/img/img_prod/740836/teclado_gamer_rgb_k_mex_rainbow_4181_1_5849b3344144db8385c4e09639e0a72f.jpg');INSERT INTO eletronicos_produto(nome, descricao, preco, quantidade, avaliacao, imagem) VALUES('Headset', 'Headset otimo para games e afins', 76, 20, 2, 'https://http2.mlstatic.com/D_NQ_NP_957830-MLA45811815046_052021-O.jpg');INSERT INTO eletronicos_produto(nome, descricao, preco, quantidade, avaliacao, imagem) VALUES('Gabinete', 'Gabinete otimo para games e afins', 10, 23, 5, 'https://m.media-amazon.com/images/I/510AwJgPr5L._AC_SY450_.jpg');INSERT INTO eletronicos_produto(nome, descricao, preco, quantidade, avaliacao, imagem) VALUES('Web cam', 'Web cam otimo para games e afins', 22, 23, 5, 'https://images-americanas.b2w.io/produtos/4548791830/imagens/novos-usb-mini-webcams-1080p-jogos-webcam-hd-1080p-computador-web-camera-com-microfone-para-gamer-pc-webcam-completo-480p/4548791830_1_large.jpg');INSERT INTO eletronicos_produto(nome, descricao, preco, quantidade, avaliacao, imagem) VALUES('Controle Xbox', 'Controle Xbox otimo para games e afins', 10, 23, 5, 'https://assets.xboxservices.com/assets/fa/b8/fab86afd-63d6-45a9-862f-798e5e45cda2.jpg?n=111101_Gallery-0_4_1350x759.jpg');",
        )
    ]