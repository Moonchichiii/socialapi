from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.pagination import PageNumberPagination

from .models import Post
from .serializers import PostSerializer
from backend.permissions import IsOwnerOrReadOnly


class PostListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination  

    def get(self, request):
        queryset = Post.objects.all().order_by('-created_at')
        query = request.query_params.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(recipe__icontains=query)
            )
        if not request.user.is_superuser:
            queryset = queryset.filter(Q(approved=True) | Q(profile=request.user.profile))

        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(paginated_queryset, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = PostSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            approved = request.user.is_superuser
            serializer.save(profile=request.user.profile, approved=approved)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublishPostView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        post.approved = True
        post.save()
        serializer = PostSerializer(post, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



class PostLikes(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        user = request.user

        if user == post.profile.user:
            return Response({'error': 'You cannot like your own post'}, status=status.HTTP_403_FORBIDDEN)

        if user not in post.likes.all():
            post.likes.add(user)
            return Response({'status': 'liked', 'likes_count': post.likes.count()}, status=status.HTTP_200_OK)
        return Response({'error': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        user = request.user

        if user not in post.likes.all():
            return Response({'error': 'Not liked'}, status=status.HTTP_400_BAD_REQUEST)

        post.likes.remove(user)
        return Response({'status': 'unliked', 'likes_count': post.likes.count()}, status=status.HTTP_200_OK)


class LikedPosts(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        posts = Post.objects.filter(likes=user).order_by('-created_at')
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
