from rest_framework.permissions import BasePermission

class HasRole(BasePermission):
    def has_permission(self, request, view):
        required_role = getattr(view, 'required_role', None)
        if not required_role:
            return True
        user_roles = request.user.user_roles.all()
        for user_role in user_roles:
            if user_role.role.name == required_role:
                return True
        return False