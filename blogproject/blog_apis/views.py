from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from blog_apis import serializers
from blog_apis import models
from rest_framework.authentication import TokenAuthentication
from blog_apis import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class UserViewSet(ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.UserModelSerializer
    queryset=models.UserModel.objects.all()
    permission_classes=(permissions.UserModelPermissions,)
    filter_backends=(filters.SearchFilter,)
    search_fields=['first_name','last_name','username','email']

class UserLoginAPiView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
class BlogsViewSet(ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.BlogModelSerializer
    queryset=models.BlogModel.objects.all()
    permission_classes=(IsAuthenticatedOrReadOnly,permissions.BlogModelPermissions)
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

    
class FollowersViewSet(ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.FollowerFollowingSerializer
    queryset=models.FollowersAndFollowing.objects.all()
    permission_classes=(permissions.FollowerFollowingPermissions,IsAuthenticatedOrReadOnly)
    def perform_create(self,serializer):
        if serializer.is_valid():
            if serializer.validated_data['following']!=self.request.user:
               serializer.save(follower=self.request.user)
            else:
                raise ValueError('the follower and following cant be same')    

class LikesVIewSet(ModelViewSet):
    authentication_classes=(TokenAuthentication,)
    serializer_class=serializers.LikesSerializer
    queryset=models.Likes.objects.all()
    permission_classes=(IsAuthenticatedOrReadOnly,)
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class SaveBlog(ModelViewSet):
    authentication_classes=(TokenAuthentication,IsAuthenticated)
    serializer_class=serializers.SavedBlogsSerializer
    queryset=models.SaveBlog.objects.all()

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)