# Generated by Django 4.1.3 on 2022-11-27 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eletronicos', '0002_produtos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='administrativo',
        ),
    ]