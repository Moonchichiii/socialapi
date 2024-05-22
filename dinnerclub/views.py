from rest_framework import generics, permissions
from .models import DinnerClub
from .serializers import DinnerClubSerializer
from backend.permissions import IsOwnerOrReadOnly

# Create your views here.


class DinnerClubListCreate(generics.ListCreateAPIView):
    queryset = DinnerClub.objects.all()
    serializer_class = DinnerClubSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user.profile)

class DinnerClubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DinnerClub.objects.all()
    serializer_class = DinnerClubSerializer
    permission_classes = [IsOwnerOrReadOnly]