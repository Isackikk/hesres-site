# ============================================================
# MODELS DA LOJA
# Aqui definimos as "classes" que representam as tabelas do banco.
# Cada classe vira uma tabela, e cada atributo vira uma coluna.
# ============================================================
from django.db import models

# ------------------------------------------------------------
# CATEGORIAS
# Tabela das categorias de produtos (ex: Limpeza, Alimentos...)
# ------------------------------------------------------------
class Categoria(models.Model):
    class Meta:
        db_table = 'categorias'  # Usa a tabela que já existe no Supabase

    nome = models.CharField(max_length=100)          # Nome da categoria
    descricao = models.TextField(blank=True, null=True)  # Descrição (pode ficar vazia)

    def __str__(self):
        return self.nome  # Mostra o nome no painel admin

# ------------------------------------------------------------
# PRODUTOS
# Tabela dos produtos da loja
# ------------------------------------------------------------
class Produto(models.Model):
    class Meta:
        db_table = 'produtos'  # Usa a tabela que já existe no Supabase

    nome = models.CharField(max_length=200)               # Nome do produto
    descricao = models.TextField(blank=True, null=True)   # Descrição do produto
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço (ex: 19.90)
    estoque = models.IntegerField(default=0)              # Quantidade em estoque
    imagem_url = models.URLField(blank=True, null=True)   # Link da foto do produto
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, related_name='produtos'
    )  # Liga o produto a uma categoria
    ativo = models.BooleanField(default=True)             # Se o produto está ativo (visível)

    def __str__(self):
        return self.nome  # Mostra o nome no painel admin

# ------------------------------------------------------------
# CLIENTES
# Tabela dos clientes da loja
# ------------------------------------------------------------
class Cliente(models.Model):
    class Meta:
        db_table = 'clientes'  # Usa a tabela que já existe no Supabase

    nome = models.CharField(max_length=200)               # Nome do cliente
    email = models.EmailField(unique=True)                # E-mail (não pode repetir)
    telefone = models.CharField(max_length=20, blank=True, null=True)  # Telefone
    cnpj_cpf = models.CharField(max_length=20, unique=True, blank=True, null=True)  # CNPJ ou CPF
    senha_hash = models.CharField(max_length=255, blank=True, null=True)  # Senha (criptografada)
    endereco = models.TextField(blank=True, null=True)    # Endereço do cliente
    criado_em = models.DateTimeField(auto_now_add=True)   # Data de criação (automática)

    def __str__(self):
        return self.nome  # Mostra o nome no painel admin

# ------------------------------------------------------------
# PEDIDOS
# Tabela dos pedidos feitos pelos clientes
# ------------------------------------------------------------
class Pedido(models.Model):
    class Meta:
        db_table = 'pedidos'  # Usa a tabela que já existe no Supabase

    # Opções de status do pedido
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name='pedidos'
    )  # Liga o pedido a um cliente
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Valor total
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')  # Status
    endereco_entrega = models.TextField(blank=True, null=True)  # Endereço de entrega
    criado_em = models.DateTimeField(auto_now_add=True)   # Data do pedido (automática)

    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente.nome}'  # Ex: "Pedido #1 - João"

# ------------------------------------------------------------
# ITENS DO PEDIDO
# Tabela dos produtos dentro de cada pedido
# ------------------------------------------------------------
class ItemPedido(models.Model):
    class Meta:
        db_table = 'itens_pedido'  # Usa a tabela que já existe no Supabase

    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, related_name='itens'
    )  # Liga o item a um pedido
    produto = models.ForeignKey(
        Produto, on_delete=models.CASCADE, related_name='itens'
    )  # Liga o item a um produto
    quantidade = models.IntegerField(default=1)            # Quantidade comprada
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Preço de cada unidade

    def __str__(self):
        return f'{self.quantidade}x {self.produto.nome}'  # Ex: "2x Detergente"