from rest_framework import serializers
from .models import Profile, CustomUser


class UserSerializer(serializers.ModelSerializer):
    '''
    Serialize the User from django inbuilt auth
    '''
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = '__all__'

class ProFileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    '''
    Serialize the profile 
    '''
    class Meta:
        model = Profile
        fields = '__all__'