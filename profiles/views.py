from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from .models import Profile
from .serializers import ProfileSerializer, CurrentUserSerializer

class ProfileList(APIView):
    """
    Profile List API View for retrieving profiles.
    """

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={"request": request})
        return Response(serializer.data)

class ProfileDetail(APIView):
    """
    Profile Detail API View for retrieving and updating profiles.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        profile = get_object_or_404(Profile, id=id)
        serializer = ProfileSerializer(profile, context={"request": request})
        return Response(serializer.data)

    def put(self, request, id):
        profile = get_object_or_404(Profile, id=id)
        serializer = ProfileSerializer(profile, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        profile = get_object_or_404(Profile, id=id)
        serializer = ProfileSerializer(profile, data=request.data, partial=True, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class CurrentUserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CurrentUserSerializer(request.user, context={"request": request})
        return Response(serializer.data)