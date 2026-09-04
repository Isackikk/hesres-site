from django.contrib import admin
from .models import Categoria, Produto

# Painel de categorias no admin do Django
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    ordering = ['nome']

# Painel de produtos no admin do Django
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'ativo', 'destaque']
    list_filter = ['categoria', 'ativo', 'destaque']
    search_fields = ['nome', 'descricao']
    list_editable = ['ativo', 'destaque']
    ordering = ['nome']