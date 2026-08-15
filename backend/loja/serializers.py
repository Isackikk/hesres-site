# ============================================================
# SERIALIZERS
# Convertem os dados do banco para JSON (formato que o front-end lê)
# ============================================================
from rest_framework import serializers
from .models import Categoria, Produto, Cliente, Pedido, ItemPedido

# ------------------------------------------------------------
# SERIALIZER DE CATEGORIA
# Converte os dados da categoria para JSON
# ------------------------------------------------------------
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao']  # Campos que vão aparecer na API

# ------------------------------------------------------------
# SERIALIZER DE PRODUTO
# Converte os dados do produto para JSON
# IMPORTANTE: NÃO mostra o preço — mostra "Preço sob consulta"
# ------------------------------------------------------------
class ProdutoSerializer(serializers.ModelSerializer):
    # Mostra o nome da categoria em vez do ID
    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)
    # Campo de aviso (não existe no banco, é fixo)
    aviso_preco = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        # Campos que vão aparecer na API (SEM o preço!)
        fields = ['id', 'nome', 'descricao', 'categoria_nome', 'imagem_url', 'ativo', 'estoque', 'aviso_preco']

    # Função que retorna o aviso de preço
    def get_aviso_preco(self, obj):
        return 'Preço sob consulta'

# ------------------------------------------------------------
# SERIALIZER DE CLIENTE
# Converte os dados do cliente para JSON
# ------------------------------------------------------------
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'telefone', 'cnpj_cpf', 'endereco', 'criado_em']

# ------------------------------------------------------------
# SERIALIZER DE ITEM DO PEDIDO
# Converte os itens do pedido para JSON
# ------------------------------------------------------------
class ItemPedidoSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source='produto.nome', read_only=True)

    class Meta:
        model = ItemPedido
        fields = ['id', 'produto_nome', 'quantidade', 'preco_unitario']

# ------------------------------------------------------------
# SERIALIZER DE PEDIDO
# Converte os dados do pedido para JSON
# ------------------------------------------------------------
class PedidoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.CharField(source='cliente.nome', read_only=True)
    itens = ItemPedidoSerializer(many=True, read_only=True)  # Mostra os itens do pedido

    class Meta:
        model = Pedido
        fields = ['id', 'cliente_nome', 'total', 'status', 'endereco_entrega', 'criado_em', 'itens']