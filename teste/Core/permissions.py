from rest_framework.permissions import BasePermission

class VerificaUsuario(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.is_authenticated == True and request.user.dono == True:
            return True
        else:
            return False