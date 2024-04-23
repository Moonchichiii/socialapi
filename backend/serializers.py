from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class InstanLoginRegisterSerializer(RegisterSerializer):
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
