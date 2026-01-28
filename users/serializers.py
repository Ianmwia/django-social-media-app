from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    '''
    Serialize the User from django inbuilt auth
    '''
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email', 'password1',]

class ProFileSerializer(serializers.ModelSerializer):
    '''
    Serialize the profile 
    '''
    class Meta:
        model = Profile
        fields = '__all__'