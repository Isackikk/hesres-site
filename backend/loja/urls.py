# ============================================================
# URLS DA API DA LOJA
# Define os endereços (rotas) da API
# ============================================================
from django.urls import path
from .views import (
    CategoriaListCreate, CategoriaDetailView,
    ProdutoListCreate, ProdutoDetailView,
    ClienteListCreate, ClienteDetailView,
    PedidoListCreate, PedidoDetailView,
)

urlpatterns = [
    # Rotas de categorias
    path('categorias/', CategoriaListCreate.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),

    # Rotas de produtos
    path('produtos/', ProdutoListCreate.as_view(), name='produto-list'),
    path('produtos/<int:pk>/', ProdutoDetailView.as_view(), name='produto-detail'),

    # Rotas de clientes
    path('clientes/', ClienteListCreate.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),

    # Rotas de pedidos
    path('pedidos/', PedidoListCreate.as_view(), name='pedido-list'),
    path('pedidos/<int:pk>/', PedidoDetailView.as_view(), name='pedido-detail'),
]