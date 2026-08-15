# ============================================================
# VIEWS (API)
# Funções que recebem as requisições do front-end e devolvem os dados
# ============================================================
from rest_framework import generics
from .models import Categoria, Produto, Cliente, Pedido
from .serializers import (
    CategoriaSerializer, ProdutoSerializer,
    ClienteSerializer, PedidoSerializer
)

# ------------------------------------------------------------
# API DE CATEGORIAS
# GET /api/categorias/        → Lista todas as categorias
# GET /api/categorias/<id>/   → Mostra uma categoria específica
# ------------------------------------------------------------
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# ------------------------------------------------------------
# API DE PRODUTOS
# GET /api/produtos/          → Lista todos os produtos ativos
# GET /api/produtos/<id>/     → Mostra um produto específico
# ------------------------------------------------------------
class ProdutoListCreate(generics.ListCreateAPIView):
    # Só mostra produtos ativos (visíveis no site)
    queryset = Produto.objects.filter(ativo=True)
    serializer_class = ProdutoSerializer

class ProdutoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

# ------------------------------------------------------------
# API DE CLIENTES
# GET /api/clientes/          → Lista todos os clientes
# POST /api/clientes/         → Cria um novo cliente
# ------------------------------------------------------------
class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# ------------------------------------------------------------
# API DE PEDIDOS
# GET /api/pedidos/           → Lista todos os pedidos
# POST /api/pedidos/          → Cria um novo pedido
# ------------------------------------------------------------
class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer