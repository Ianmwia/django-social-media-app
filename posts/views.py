from django.shortcuts import render, redirect

#serializers for api endpoints
from rest_framework import viewsets
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from .forms import PostForm

# Create your views here.
#class based api views
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create_post_author(self, serializer):
        #set the logged in user as author of the post
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        #add a comment
        post = self.get_object()
        comment_text = request.data.get('comment')
        if not comment_text:
            return Response({'error':'Comment Text is required'})
        

        #create a comment
        comment = Comment.objects.create(user=request.user, post=post, comment=comment_text)
        comment_serializer = CommentSerializer(comment)
        return Response(comment_serializer.data)
    

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        like, created = Like.objects.get_or_create(user=user, post=post)

        if created:
            return Response({'status': 'Liked'})
        else:
            return Response({'status': 'Already liked'})



class CommentViewSet(viewsets.ModelViewSet):
    '''
    Docstring for CommentViewSet
    To get a single comment do not use objects.all get by post_id
    '''
    serializer_class = CommentSerializer
    def get_queryset(self):
        #get comments for a specific post
        post_id = self.kwargs.get('post_id')
        if post_id:
            return Comment.objects.filter(post_id=post_id)
        return Comment.objects.all()


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


# normal views
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
             # ensure text is must no blank posts
            if not form.cleaned_data.get('text_post'):
                form.add_error('text_post', "Text input field cannot be empty")
                return render(request, 'create_post.html', {'form':form})
        
            form.save(user=request.user)
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form':form})

def news_feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'news_feed.html', {'posts':posts})