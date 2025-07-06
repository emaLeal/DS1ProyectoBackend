# permissions.py
from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.id is not 3

class IsTalentDirector(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.id == 2

class IsPostulant(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role.id == 3

class CanManageInternalUsers(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        role_name = request.user.role.name
        if request.method == 'DELETE':
            return role_name == 'admin'
        return role_name in ['admin', 'director_talento']
