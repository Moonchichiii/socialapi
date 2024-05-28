from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer
from backend.permissions import IsOwnerOrReadOnly

class ProfileList(APIView):
    permission_classes = [IsAuthenticated]
    """
    API view for listing profiles.
    """

    def get(self, request):
        """
        Get the queryset of profiles, sorted by 'most_liked' posts.
        """
        queryset = Profile.objects.annotate(
            total_likes=Count('posts__likes', distinct=True)
        ).order_by('-total_likes')
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    API view for retrieving and updating a profile.
    """
    permission_classes = [IsOwnerOrReadOnly,IsAuthenticated]

    def get_object(self, pk):
        """
        Get the profile object based on the provided pk.
        """
        profile = get_object_or_404(Profile, pk=pk)
        self.check_object_permissions(self.request, profile)
        return profile

    def get(self, request, pk):
        """
        Get the serialized data of the profile.
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        """
        Update the profile with the provided data.
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
