from rest_framework import serializers
from .models import Profile,Post

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'email', 'profile_photo')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('name', 'site_link', 'description')