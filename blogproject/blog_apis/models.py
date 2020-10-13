from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth .models import BaseUserManager
from rest_framework.authtoken.models import Token
from django.utils import timezone
# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,email,password,first_name,last_name,username,date_of_birth,**extra_fields):
        if email==None or first_name==None or last_name==None or username==None or date_of_birth==None:
            raise ValueError('Please provide all the valid credients')
        else:
            email=self.normalize_email(email)
            user=self.model(email=email,
            first_name=first_name,
            last_name=last_name,
            username=username,
            date_of_birth=date_of_birth)
            user.set_password(password)
            user.save(using=self._db)
            token=Token.objects.create(user=user)

            return user
    
    def create_superuser(self,email,password,first_name,last_name,username,date_of_birth,**extra_fields):
        user=self.create_user(email,password,first_name,last_name,username,date_of_birth)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)


class UserModel(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True)
    username=models.CharField(unique=True,max_length=255)
    date_of_birth=models.DateField()
    is_staff=models.BooleanField(default=False)
    #followers=models.ManyToManyField('self',related_name='followers',blank=True)
    #following_data=models.ManyToManyField('self',related_name='followings',blank=True)

    objects=UserProfileManager()

    REQUIRED_FIELDS=['first_name','last_name','date_of_birth','username']
    USERNAME_FIELD='email'

    def __str__(self):
        return self.username

class FollowersAndFollowing(models.Model):
    follower=models.ForeignKey(UserModel,related_name='follower',on_delete=models.CASCADE)
    following=models.ForeignKey(UserModel,related_name='following',on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together=('follower','following')
        ordering=('-created',)
    def __str__(self):
        return f"{self.follower} following {self.following}"   

def upload_to(instance,filename):
    return '/'.join(['products',str(instance.id),filename])

class BlogModel(models.Model):
    title=models.CharField(max_length=255)
    content=models.CharField(max_length=510)
    author=models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='author')
    category=models.CharField(max_length=40)
    isAdultOnly=models.BooleanField(default=False)
    create=models.DateTimeField(default=timezone.now(),)
    class Meta:
        unique_together=('author','content')
        ordering=['-create']
    
    def __str__(self):
        return self.title



    



class Likes(models.Model):
    user=models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='user')
    post=models.ForeignKey(BlogModel,on_delete=models.CASCADE,related_name='post')
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together=('user','post')
        ordering=['-created']

    def __str__(self):
        return f"{self.user} likes {self.post}"   
class SaveBlog(models.Model):
    blog=models.ForeignKey(BlogModel,on_delete=models.CASCADE)
    user=models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='usersaved')
    saved=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together=('blog','user')
        ordering=['-saved']