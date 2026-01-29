from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

#serializers router path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register(r'', views.PostViewSet, basename='post')
router.register(r'comment', views.CommentViewSet, basename='comment')
router.register(r'like', views.LikeViewSet, basename='like')

urlpatterns = [
    #api router urls
    path("", include(router.urls)),
    
    #path("register", views.register, name='register'),
    path("create_post", views.create_post, name='create_post'),
    path("feed", views.news_feed, name='feed'),
    
]