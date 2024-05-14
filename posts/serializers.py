from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the Post model."""

    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')
    display_name = serializers.ReadOnlyField(source='profile.display_name')
    is_superuser = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    approved = serializers.BooleanField(read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'display_name', 'profile_id', 'profile_image',
            'title', 'ingredients', 'recipe', 'description',
            'cooking_time', 'image', 'created_at', 'updated_at',
            'is_owner', 'likes_count', 'is_superuser', 'approved'
        ]

    def get_is_owner(self, obj):
        """Check if the request user is the owner of the post."""
        request = self.context.get('request')
        return request.user == obj.profile.user if request else False

    def get_is_superuser(self, obj):
        """Check if the request user is a superuser."""
        request = self.context.get('request')
        return request.user.is_superuser if request else False
    
    def get_likes_count(self, obj):
        return obj.likes.count()

    def validate_image(self, value):
        """Validate the size and dimensions of the image."""
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height greater than 4096px!')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width greater than 4096px!')
        return value