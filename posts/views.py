from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from backend.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated 
from .models import Post, Like
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination


from rest_framework.throttling import UserRateThrottle

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BurstRateThrottle(UserRateThrottle):
      scope = 'burst'
      

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination
    throttle_classes = [BurstRateThrottle]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ingredients','title', 'created_at']

    def perform_create(self, serializer):
       
        serializer.save(profile=self.request.user.profile)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        """
     
        """
        pk = self.kwargs.get('pk')
        return get_object_or_404(Post, pk=pk)

    def put(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LikeView(generics.GenericAPIView):
  
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            return Response({'message': 'Liked!'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Only Possible to like it once!'}, status=status.HTTP_409_CONFLICT)

    def delete(self, request, post_id):
        like = get_object_or_404(Like, user=request.user, post_id=post_id)
        like.delete()
        return Response({'message': 'Like removed!'}, status=status.HTTP_204_NO_CONTENT)