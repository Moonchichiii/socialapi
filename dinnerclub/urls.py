from django.urls import path
from .views import DinnerClubListCreate, DinnerClubDetail

urlpatterns = [
 path('', DinnerClubListCreate.as_view(), name='dinner-club-list-create'),
 path('<int:pk>/', DinnerClubDetail.as_view(), name='dinner-club-detail'),
]