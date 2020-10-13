from rest_framework import serializers
from blog_apis import models

class FollowingSerialzer(serializers.ModelSerializer):
    class Meta:
        model=models.FollowersAndFollowing
        fields=('id','following','created')
        depth=1
        
class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.FollowersAndFollowing
        fields=('id','follower','created')
        depth=1

class UserBlogs(serializers.ModelSerializer):
    class Meta:
        model=models.BlogModel
        fields=('id','title','content','isAdultOnly')

class SavedBlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.SaveBlog
        fields='__all__'
        extra_kwargs={'user':{'read_only':'true'}}

class UserModelSerializer(serializers.ModelSerializer):
    following_data=serializers.SerializerMethodField()
    followers_data=serializers.SerializerMethodField()
    blogs=serializers.SerializerMethodField()
    saved_blogs=serializers.SerializerMethodField()
    class Meta:
        model=models.UserModel
        fields=('id','first_name','last_name','email','username','password','date_of_birth','following_data','followers_data','blogs','saved_blogs')
        extra_kwargs={
            'password':{'write_only':'true'}
        }
    def get_following_data(self,obj):
        return FollowingSerialzer(obj.follower.all(),many=True).data
    
    def get_followers_data(self,obj):
        return FollowersSerializer(obj.following.all(),many=True).data
    def get_blogs(self,obj):
        return UserBlogs(obj.author.all(),many=True).data
    def get_saved_blogs(self,obj):
        return SavedBlogsSerializer(obj.usersaved.all(),many=True).data

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Likes
        extra_kwargs={'user':{'read_only':'true'}}
        fields='__all__'
    


class BlogModelSerializer(serializers.ModelSerializer):
    author=UserModelSerializer(read_only=True)
    likes=serializers.SerializerMethodField()
    class Meta:
        model=models.BlogModel
        fields=('id','title','content','author','category','isAdultOnly','create','likes')
    def get_likes(self,obj):
        return LikesSerializer(obj.post.all(),many=True).data    

class FollowerFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.FollowersAndFollowing
        fields='__all__'
        extra_kwargs={'follower':{'read_only':'true'}}

