from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext_lazy as _
#from users.models import CustomUser
from django.conf import settings


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text_post = models.TextField(_("content"), blank=True)
    image_post = CloudinaryField(_("image post"), blank=True)
    created_at = models.DateTimeField(_("date post was created"), auto_now_add=True)


class Comment(models.Model):
    '''
    get foreign key from Post
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("get user post"), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, blank=True, related_name='comment', on_delete=models.CASCADE)
    comment = models.TextField(_("comment"))



class Like(models.Model):
    '''
    get foreign key from Post 
    get user foreign key from Custom User
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(""), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, blank=True, related_name='like', on_delete=models.CASCADE)
