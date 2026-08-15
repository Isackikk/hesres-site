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
# GET /api/produtos/          → Lista produtos (admin vê todos, cliente só ativos)
# GET /api/produtos/<id>/     → Mostra um produto específico
# ------------------------------------------------------------
class ProdutoListCreate(generics.ListCreateAPIView):
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        # Se for admin logado → mostra TODOS os produtos (inclusive inativos)
        if self.request.user.is_staff:
            return Produto.objects.all()
        # Se for cliente comum → só mostra produtos ativos
        return Produto.objects.filter(ativo=True)

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