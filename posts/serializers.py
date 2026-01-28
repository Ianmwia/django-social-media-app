from rest_framework import serializers
from .models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    '''
    Serialize the Posts
    '''
    class Meta:
        model = Post
        fields = '__all__'

        
class CommentSerializer(serializers.ModelSerializer):
    '''
    Serialize the Comment
    '''
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    '''
    Serialize the Like
    '''
    class Meta:
        model = Like
        fields = '__all__'
