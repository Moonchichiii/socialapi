from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from profiles.models import Profile
from .models import Follower
from .serializers import FollowerSerializer

class FollowersListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerSerializer

    def get_queryset(self):
        user_profile = get_object_or_404(Profile, user=self.request.user)
        return Follower.objects.filter(profile=user_profile).order_by('-created_at')

class FollowingListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerSerializer

    def get_queryset(self):
        user_profile = get_object_or_404(Profile, user=self.request.user)
        return Follower.objects.filter(follower=user_profile).order_by('-created_at')

class FollowUnfollowView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerSerializer

    def post(self, request, profile_id):
        profile_to_follow = get_object_or_404(Profile, id=profile_id)
        user_profile = get_object_or_404(Profile, user=request.user)

        if Follower.objects.filter(follower=user_profile, profile=profile_to_follow).exists():
            return Response({"detail": "You are already following this profile."}, status=status.HTTP_400_BAD_REQUEST)

        follower_instance = Follower(follower=user_profile, profile=profile_to_follow)
        follower_instance.save()
        return Response({"detail": "Successfully followed the profile."}, status=status.HTTP_201_CREATED)

    def delete(self, request, profile_id):
        profile_to_unfollow = get_object_or_404(Profile, id=profile_id)
        user_profile = get_object_or_404(Profile, user=request.user)

        follower_instance = Follower.objects.filter(follower=user_profile, profile=profile_to_unfollow)
        if follower_instance.exists():
            follower_instance.delete()
            return Response({"detail": "Successfully unfollowed the profile."}, status=status.HTTP_204_NO_CONTENT)

        return Response({"detail": "You are not following this profile."}, status=status.HTTP_400_BAD_REQUEST)