# ============================================================
# URLS DA API DA LOJA
# Define os endereços (rotas) da API
# ============================================================
from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.api_produtos, name='api_produtos'),
    path('produtos/<int:id>/', views.api_produtos, name='api_produto_detalhe'),
    path('destaque/', views.api_destaque, name='api_destaque'),
    path('categorias/', views.api_categorias, name='api_categorias'),
]