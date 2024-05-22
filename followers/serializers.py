from rest_framework import serializers
from profiles.serializers import ProfileSerializer
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    follower = ProfileSerializer(read_only=True)
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Follower
        fields = ['id', 'follower', 'profile', 'created_at']