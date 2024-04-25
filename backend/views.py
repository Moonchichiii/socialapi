from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationSerializer

@api_view(['GET'])
def root_route(request):
    return Response({
        'message': "Welcome to the Social App API!",
    })

@api_view(['POST'])
def Register(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            data = {
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                },
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)