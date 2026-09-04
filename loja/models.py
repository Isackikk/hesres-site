from django.db import models

class Categoria(models.Model):
    """Categoria de produtos (ex: Limpeza, Alimentos, Higiene)"""
    nome = models.CharField(max_length=100, verbose_name='Nome')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Produto(models.Model):
    """Produto do catálogo da HES Atacado"""
    nome = models.CharField(max_length=200, verbose_name='Nome')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    imagem = models.URLField(max_length=500, blank=True, null=True, verbose_name='URL da imagem')
    estoque = models.IntegerField(default=0, verbose_name='Estoque')
    ativo = models.BooleanField(default=True, verbose_name='Ativo (visível no site)')
    destaque = models.BooleanField(default=False, verbose_name='Destaque (destaque para clientes logados)')
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='produtos',
        verbose_name='Categoria'
    )
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']

    def __str__(self):
        return self.nome