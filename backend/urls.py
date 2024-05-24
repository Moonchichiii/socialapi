from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import root_route,register,current_user, logout, login
# Api routes.
urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    
    path('api/login/', login, name='login'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', register, name='register'),
    path('api/logout/', logout, name='logout'),
    path('api/current-user/', current_user, name='current_user'),
    
    path('api/profiles/', include('profiles.urls'), name='profiles'),
    path('api/posts/', include('posts.urls'), name='posts'),
    path('api/comments/', include('comments.urls'), name='comments'),
    path('api/followers/', include('followers.urls'), name='followers'),
   
]