from django.urls import path
from .views import FollowersList, FollowersDetail

urlpatterns = [
    path('', FollowersList.as_view(), name='followers-list'),
    path('<int:profile_id>/follow/', FollowersDetail.as_view(), name='follow-profile'),
    path('<int:profile_id>/unfollow/', FollowersDetail.as_view(), name='unfollow-profile'),
]
