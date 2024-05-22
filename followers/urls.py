from django.urls import path
from .views import FollowerListCreateView, FollowerDetailView

urlpatterns = [
    path('', FollowerListCreateView.as_view(), name='follower-list-create'),
    path('<int:pk>/', FollowerDetailView.as_view(), name='follower-detail'),
]
