# ============================================================
# URLS PRINCIPAIS DO PROJETO
# Conecta as rotas da API e do painel admin
# ============================================================
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),        # Painel administrativo
    path('api/', include('loja.urls')),      # API da loja (todas as rotas começam com /api/)
]