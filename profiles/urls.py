from django.urls import path
from .views import ProfileList, ProfileDetail

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:id>/', ProfileDetail.as_view(), name='profile-detail'),
]