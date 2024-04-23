from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(RegisterSerializer):
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        return data_dict

    def save(self, request):
        user = super().save(request)
        refresh = RefreshToken.for_user(user)
        return {
            'user': {
                'username': user.username,
                'email': user.email
            },
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh)
        }


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )