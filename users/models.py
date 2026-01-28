from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True, blank=True)
    bio = models.TextField(_("persons biography"), blank=True)

    def __str__(self):
        return self.user.username