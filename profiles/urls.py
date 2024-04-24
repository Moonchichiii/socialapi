from django.urls import path
from .views import ProfileList, ProfileDetail, CurrentUserProfile

urlpatterns = [
    path('', ProfileList.as_view(), name='profile-list'),
    path('<int:id>/', ProfileDetail.as_view(), name='profile-detail'),
    path('current/', CurrentUserProfile.as_view(), name='current-user-profile'),
]