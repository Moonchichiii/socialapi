from rest_framework import serializers
from .models import Post, Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta:
        model = Post
        fields = ['id', 'profile_id', 'profile_image', 'title', 'ingredients', 'recipe', 'description', 'cooking_time', 'image', 'created_at', 'updated_at']

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.profile.user if request else False

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height greater than 4096px!')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width greater than 4096px!')
        return value
