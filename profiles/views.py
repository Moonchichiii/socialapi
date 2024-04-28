from rest_framework import generics, status
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from backend.permissions import IsOwnerOrReadOnly   

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
  
class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        pk = self.kwargs.get('pk', None)
        if pk == "current":
            try:
                
                return Profile.objects.get(owner=self.request.user)
            except Profile.DoesNotExist:
                
                raise generics.Http404("No Profile matches the given query.")
        return super().get_object()

    