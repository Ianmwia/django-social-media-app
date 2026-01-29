from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text_post','image_post']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['text_post'].widget.attrs.update({
            'class': 'h-[100px] w-auto outline rounded mb-2 p-1 bg-white'
        })
        self.fields['image_post'].widget.attrs.update({
            'class': 'w-auto outline rounded mb-2 p-1 bg-white items-center hover:cursor-pointer'
        })

    def save(self, user, commit=True):
        post = super().save(commit=False)
        post.author = user
        if commit:
            post.save()
        return post