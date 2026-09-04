from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Produto, Categoria

def serialize_produto(p):
    return {
        'id': p.id,
        'nome': p.nome,
        'descricao': p.descricao,
        'imagem': p.imagem if p.imagem else None,
        'ativo': p.ativo,
        'destaque': p.destaque,
        'categoria_id': p.categoria.id if p.categoria else None,
        'categoria_nome': p.categoria.nome if p.categoria else None,
    }

def serialize_categoria(c):
    return {
        'id': c.id,
        'nome': c.nome,
    }

# API — Lista todos os produtos ou busca um especifico
@csrf_exempt
def api_produtos(request, id=None):
    if id:
        try:
            p = Produto.objects.get(id=id, ativo=True)
            return JsonResponse(serialize_produto(p))
        except Produto.DoesNotExist:
            return JsonResponse({'erro': 'Produto nao encontrado'}, status=404)

    produtos = Produto.objects.filter(ativo=True).order_by('nome')
    return JsonResponse([serialize_produto(p) for p in produtos], safe=False)

# API — Produtos em destaque
@csrf_exempt
def api_destaque(request):
    produtos = Produto.objects.filter(ativo=True, destaque=True).order_by('nome')
    return JsonResponse([serialize_produto(p) for p in produtos], safe=False)

# API — Categorias
@csrf_exempt
def api_categorias(request):
    categorias = Categoria.objects.all().order_by('nome')
    return JsonResponse([serialize_categoria(c) for c in categorias], safe=False)