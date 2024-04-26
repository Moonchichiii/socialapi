from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Profile
from backend.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
  

class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        pk = self.kwargs.get('pk')
        if pk == "current":
            return get_object_or_404(Profile, owner=self.request.user)
        return super().get_object()
