from django.shortcuts import render

#serializers for api endpoints
from rest_framework import viewsets
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer

# Create your views here.
#class based api views
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    '''
    Docstring for CommentViewSet
    To get a single comment do not use objects.all get by post_id
    '''
    serializer_class = CommentSerializer
    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if post_id:
            return Comment.objects.filter(post_id=post_id)
        return Comment.objects.all()


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


