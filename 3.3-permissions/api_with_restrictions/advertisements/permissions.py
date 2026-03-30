from rest_framework.permissions import BasePermission, IsAuthenticated


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        if request.user.is_staff == True:
            return True
        return request.user == obj.creator
