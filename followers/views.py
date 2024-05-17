from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles.models import Profile
from .models import Follower
from .serializers import FollowerSerializer
from backend.permissions import IsOwnerOrReadOnly

class FollowersList(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def get(self, request, *args, **kwargs):
        followers = Follower.objects.filter(profile__user=request.user)
        serializer = self.serializer_class(followers, many=True)
        return Response(serializer.data)

class FollowersDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def post(self, request, profile_id):
        profile = get_object_or_404(Profile, pk=profile_id)
        Follower.objects.create(user=request.user, profile=profile)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, profile_id):
        profile = get_object_or_404(Profile, pk=profile_id)
        Follower.objects.filter(user=request.user, profile=profile).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
