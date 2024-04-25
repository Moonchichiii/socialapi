from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profiles.
    """
    owner = serializers.ReadOnlyField(source='owner.username')    

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'created_at', 'name', 'content', 'image']

    def get_is_owner(self, obj):      
        return obj.owner == self.context['request'].user

class CurrentUserSerializer(UserDetailsSerializer):
    owner_id = serializers.ReadOnlyField(source='profile.id')
    owner_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('owner_id', 'owner_image',)