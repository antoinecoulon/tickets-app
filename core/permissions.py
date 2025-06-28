from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'
    
class IsAgent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'agent'
    
class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'client'
    
# TICKETS
class IsTicketOwnerOrAdmin(permissions.BasePermission):
    """
    Permission pour vérifier que l'utilisateur est:
    - soit le créateur du ticket (client)
    - soit un admin
    """
    def has_object_permission(self, request, view, obj):
        return obj.client == request.user or request.user.role == 'admin'
    
class IsInSameCompanyAsTicket(permissions.BasePermission):
    """
    Permission pour les agents: vérifier que le ticket appartient à leur entreprise
    """
    def has_object_permission(self, request, view, obj):
        return request.user.role == 'agent' and obj.client.entreprise == request.user.entreprise
    
# MESSAGES
class CanViewMessage(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.role == 'admin':
            return True
        if user.role == 'client':
            return obj.ticket.client == user
        if user.role == 'agent':
            return obj.ticket.client.entreprise == user.entreprise
        return False
    
class CanPostMessage(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    """ Empêche d’associer un message à un ticket non autorisé """
    def has_object_permission(self, request, view, obj):
        return True
