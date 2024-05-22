from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from django.http import Http404
from django.contrib.auth import get_user_model

from .serializers import RegistrationSerializer,LoginSerializer, CurrentUserSerializer

@api_view(['GET'])
def root_route(request):
    """
    DRF root route.
    """ 
    return Response({"message": "Welcome to the Social App API!"})

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    Custom user registration, handing out tokens instantly for new users for immediate login.
    """
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        response = Response({
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user_id': user.id
        }, status=status.HTTP_201_CREATED)
        response.set_cookie(
            settings.JWT_AUTH_COOKIE,
            access_token,
            httponly=True,
            secure=settings.JWT_AUTH_COOKIE_SECURE,
            samesite='None',
        )
        response.set_cookie(
            settings.JWT_REFRESH_AUTH_COOKIE,
            refresh_token,
            httponly=True,
            secure=settings.JWT_AUTH_COOKIE_SECURE,
            samesite='None',
        )
        return response
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    User login view.
    """
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        response = Response({
            'access_token': access_token,
            'refresh_token': refresh_token,
        }, status=status.HTTP_200_OK)
        response.set_cookie(
            settings.JWT_AUTH_COOKIE,
            access_token,
            httponly=True,
            secure=settings.JWT_AUTH_COOKIE_SECURE,
            samesite='None',
        )
        response.set_cookie(
            settings.JWT_REFRESH_AUTH_COOKIE,
            refresh_token,
            httponly=True,
            secure=settings.JWT_AUTH_COOKIE_SECURE,
            samesite='None',
        )
        return response
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    """
    User logout and blacklist refresh token.
    """
    try:
        refresh_token = request.COOKIES.get(settings.JWT_REFRESH_AUTH_COOKIE)
        token = RefreshToken(refresh_token)
        token.blacklist()
        response = Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
        response.delete_cookie(settings.JWT_AUTH_COOKIE)
        response.delete_cookie(settings.JWT_REFRESH_AUTH_COOKIE)
        return response
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user_id = request.user.id
    User = get_user_model()
    try:
        user = User.objects.select_related('profile').get(id=user_id)
        serializer = CurrentUserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        raise Http404("User not found")