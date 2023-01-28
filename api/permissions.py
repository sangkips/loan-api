from rest_framework import permissions

"""  
# allows creator to to have permissions to see the contents of the app
class IsOwner(permissions.BasePermission):
    status = "Permission denied"

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
"""


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
