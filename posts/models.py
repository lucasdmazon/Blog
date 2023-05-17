from django.db import models
from categorias.models import Categoria
from django.utils import timezone


class Post(models.Model):
    nome_post = models.CharField(max_length=255, verbose_name='Título')
    empresa_post = models.CharField(max_length=255, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo_post = models.TextField(verbose_name='Conteúdo')
    excerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Categoria')
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Imagem')
    publicado_post = models.BooleanField(default=False, verbose_name='Publicado')


    def __str__(self):
        return self.nome_post

"""
user: administrador
password: 123456
"""