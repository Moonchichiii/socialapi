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