from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.shortcuts import get_object_or_404
from posts.models import Post
from .models import Comment
from .serializers import CommentSerializer
from backend.permissions import IsOwnerOrReadOnly

class CommentListCreateView(APIView):
    """
    API view for listing and creating comments.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, post_id):
        """
        Get all comments for a specific post.
        """
        comments = Comment.objects.filter(post_id=post_id).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, post_id):
        """
        Create a new comment for a specific post.
        """
        post = get_object_or_404(Post, pk=post_id)
        data = request.data
        serializer = CommentSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save(profile=request.user.profile, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):
    """
    API view for retrieving, updating, and deleting a comment.
    """
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request, post_id, pk):
        """
        Get a specific comment for a post.
        """
        comment = get_object_or_404(Comment, post_id=post_id, pk=pk)
        serializer = CommentSerializer(comment, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, post_id, pk):
        """
        Update a specific comment for a post.
        """
        comment = get_object_or_404(Comment, post_id=post_id, pk=pk)
        self.check_object_permissions(request, comment)
        serializer = CommentSerializer(comment, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, post_id, pk):
        """
        Partially update a specific comment for a post.
        """
        comment = get_object_or_404(Comment, post_id=post_id, pk=pk)
        self.check_object_permissions(request, comment)
        serializer = CommentSerializer(comment, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, pk):
        """
        Delete a specific comment for a post.
        """
        comment = get_object_or_404(Comment, post_id=post_id, pk=pk)
        self.check_object_permissions(request, comment)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
