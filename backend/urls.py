from django.contrib import admin
from django.urls import path,include
from .views import root_route


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_route, name='root_route'),
    
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    
    path('', include('profiles.urls')),
]
