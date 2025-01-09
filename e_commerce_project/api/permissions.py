from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Allow GET, HEAD, OPTIONS
        return request.user and request.user.is_authenticated

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
    

class IsSelfOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj): 
         # Permission checks for safe methods (GET, OPTIONS, HEAD)
         if request.method in SAFE_METHODS:
             return obj == request.user or request.user.is_staff 
         return False