from rest_framework.permissions import BasePermission

class UserIsOwnerTodo(BasePermission):

    def has_object_permission(self, request, view, cat):
        return request.user.id == cat.user.id