from django.urls import path
from .views import PostListCreateView, PostDetailView, PostLikes, LikedPosts

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/post-likes/', PostLikes.as_view(), name='toggle-like'),
    path('liked-posts/', LikedPosts.as_view(), name='liked-posts'),
]
