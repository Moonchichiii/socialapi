from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    total_likes = serializers.IntegerField(read_only=True)
    profile_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Profile
        fields = ['profile_id', 'user', 'display_name', 'bio', 'image', 'created_at', 'updated_at', 'total_likes']
        read_only_fields = ['user', 'created_at', 'updated_at', 'total_likes']

    def update(self, instance, validated_data):
        instance.display_name = validated_data.get('display_name', instance.display_name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
