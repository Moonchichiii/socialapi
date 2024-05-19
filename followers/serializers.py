from rest_framework import serializers
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    follower_display_name = serializers.ReadOnlyField(source='follower.display_name')
    follower_profile_image = serializers.ReadOnlyField(source='follower.image.url')
    profile_display_name = serializers.ReadOnlyField(source='profile.display_name')
    profile_profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta:
        model = Follower
        fields = ['id', 'profile', 'follower', 'follower_display_name', 'follower_profile_image', 'profile_display_name', 'profile_profile_image', 'created_at']
        read_only_fields = ['id', 'created_at', 'follower_display_name', 'follower_profile_image', 'profile_display_name', 'profile_profile_image']

    def create(self, validated_data):
        return Follower.objects.create(**validated_data)
