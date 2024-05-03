from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """
    class Meta:
      
        model = Profile
        fields = ['user', 'display_name', 'bio', 'image', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

      
    def update(self, instance, validated_data):
        instance.display_name = validated_data.get('display_name', instance.display_name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
