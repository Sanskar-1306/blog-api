from blog_apis import views
from django.urls import include,path
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('users',views.UserViewSet)
router.register('blogs',views.BlogsViewSet)
router.register('followers',views.FollowersViewSet)
router.register('like_blog',views.LikesVIewSet)
router.register('save_blog',views.SaveBlog)
urlpatterns=[path('',include(router.urls)),
             path('login/',views.UserLoginAPiView.as_view()),]