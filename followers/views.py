from django.shortcuts import get_object_or_404
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from profiles.models import Profile
from .models import Follower
from .serializers import FollowerSerializer

class FollowerListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Follower.objects.all().order_by('-created_at')
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        profile_id = self.request.data.get('profile_id')
        
        if not profile_id:
            raise serializers.ValidationError({"detail": "Profile ID is required!"})
        profile_to_follow = get_object_or_404(Profile, id=profile_id)
        if profile_to_follow.user == self.request.user:
            raise serializers.ValidationError({"detail": "You can't follow yourself!"})
        if Follower.objects.filter(follower=self.request.user.profile, profile=profile_to_follow).exists():
            raise serializers.ValidationError({"detail": "You are already following this profile!"})
        serializer.save(follower=self.request.user.profile, profile=profile_to_follow)

class FollowerDetailView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Follower.objects.all().order_by('-created_at')
    serializer_class = FollowerSerializer

    def delete(self, request, *args, **kwargs):
        profile_to_unfollow = get_object_or_404(Profile, id=kwargs['pk'])
        follower_instance = get_object_or_404(Follower, follower=request.user.profile, profile=profile_to_unfollow)
        follower_instance.delete()
        return Response({"detail": "Success!"}, status=status.HTTP_204_NO_CONTENT)