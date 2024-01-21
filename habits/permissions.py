from rest_framework.permissions import BasePermission


class IsAutor(BasePermission):
    """ Проверка на автора """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
