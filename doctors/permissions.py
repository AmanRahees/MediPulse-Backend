from rest_framework import permissions

class isDoctor(permissions.BasePermission):
    message = 'Only Doctors Allowed.'
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == "doctor"
        return False