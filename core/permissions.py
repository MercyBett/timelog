from rest_framework import permissions




class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
      """
      If the request is a safe method (GET, HEAD, OPTIONS), then return True

      :param request: The request object
      :param view: The view that is calling the permission class
      :param obj: The object that the user is trying to access
      :return: The return value is a boolean value.
      """

      if request.method in permissions.SAFE_METHODS:
          return True

      if has_admin_attr := hasattr(request.user, 'is_staff'):
          return request.user.is_staff == True or obj.user == request.user
      return obj.user == request.user


class IsOwnerOrAdmin(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
      """
      If the user has the attribute 'is_staff', then return True if the user is a staff member,
      otherwise return True if the user is the owner of the object

      :param request: The request object
      :param view: The view that is calling the permission class
      :param obj: The object that the permission is being checked against
      :return: The return value is a boolean.
      """

      if has_admin_attr := hasattr(request.user, 'is_staff'):
          return request.user.is_staff == True or obj.user == request.user
      return obj.user == request.user



