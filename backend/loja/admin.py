from django.contrib import admin
from .models import Categoria, Produto, Cliente, Pedido, ItemPedido

# Painel de Categorias
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')  # Colunas que aparecem na lista
    search_fields = ('nome',)  # Campo de busca

# Painel de Produtos
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'estoque', 'ativo')
    list_filter = ('categoria', 'ativo')  # Filtro lateral
    search_fields = ('nome', 'descricao')

# Painel de Clientes
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cnpj_cpf')
    search_fields = ('nome', 'email', 'cnpj_cpf')

# Painel de Pedidos
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'status', 'total', 'criado_em')
    list_filter = ('status',)  # Filtro por status
    search_fields = ('cliente__nome',)

# Painel de Itens do Pedido
@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto', 'quantidade', 'preco_unitario')
    search_fields = ('produto__nome',)