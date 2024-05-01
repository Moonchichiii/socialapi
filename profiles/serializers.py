from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'display_name', 'bio', 'image']