
from django.urls import path
from .views import PostListCreateView, PostDetailView, LikeView

urlpatterns = [
    path('', PostListCreateView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('<int:post_id>/like/', LikeView.as_view(), name='like-post'),
]
