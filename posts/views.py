from rest_framework import generics
from .permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

from backend.permissions import IsOwnerOrReadOnly
# Create your views here.


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(profile=profile)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]