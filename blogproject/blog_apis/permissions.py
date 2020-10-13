from rest_framework import permissions

class UserModelPermissions(permissions.BasePermission):
    def has_object_permission(self,request,view,object):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return object.id==request.user.id


class BlogModelPermissions(permissions.BasePermission):
    def has_object_permission(self,request,view,object):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return object.author.id==request.user.id
class FollowerFollowingPermissions(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.id==obj.follower.id or request.user.id == obj.following.id    
    