from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationSerializer

@api_view(['GET'])
def root_route(request):
    return Response({
        'message': "Welcome to the Social App API!",
    })

@api_view(['POST'])
def Register(request):
    
    if User.objects.filter(username=request.data.get('username')).exists():
        return Response({"username": "A user with that username already exists."}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=request.data.get('email')).exists():
        return Response({"email": "A user with that email already exists."}, status=status.HTTP_400_BAD_REQUEST)

    
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user, refresh = serializer.save()
        
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
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
