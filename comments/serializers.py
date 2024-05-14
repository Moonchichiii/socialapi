from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')
    display_name = serializers.ReadOnlyField(source='profile.display_name')
    post_id = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Comment
        fields = ['id', 'profile_id', 'profile_image', 'display_name', 'post_id', 'text', 'created_at', 'updated_at']
        read_only_fields = ['id', 'profile_id', 'profile_image', 'display_name', 'post_id', 'created_at', 'updated_at']
