from django.urls import path
from .views import FollowersListView, FollowingListView, FollowUnfollowView

urlpatterns = [
    path('', FollowersListView.as_view(), name='followers-list'),
    path('following/', FollowingListView.as_view(), name='following-list'),
    path('<int:profile_id>/', FollowUnfollowView.as_view(), name='follow-unfollow-profile'),
]
