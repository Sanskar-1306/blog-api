from django.contrib import admin
from blog_apis import models
# Register your models here.
admin.site.register(models.UserModel)
admin.site.register(models.BlogModel)
admin.site.register(models.FollowersAndFollowing)
admin.site.register(models.Likes)