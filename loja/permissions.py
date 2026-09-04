from rest_framework.permissions import BasePermission

# Permissão customizada:
# - Qualquer pessoa pode VER os produtos (GET)
# - Só o admin pode cadastrar, editar e excluir (POST, PUT, DELETE)
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS → qualquer um pode acessar
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # POST, PUT, PATCH, DELETE → só admin logado
        return request.user and request.user.is_staff