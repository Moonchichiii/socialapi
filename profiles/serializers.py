from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_id = serializers.SerializerMethodField()
    owner_image = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'created_at', 'name', 'content', 'image', 'owner_id', 'owner_image']

    def get_owner_id(self, obj):
        return obj.owner.id if self.context.get('request').user == obj.owner else None

    def get_owner_image(self, obj):
        return obj.image.url if obj.image and self.context.get('request').user == obj.owner else None

    def validate_name(self, value):
        if Profile.objects.filter(name=value).exclude(id=self.instance.id).exists():
            raise serializers.ValidationError("Sorry the username is already in use.")
        return value

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.content = validated_data.get('content', instance.content)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
