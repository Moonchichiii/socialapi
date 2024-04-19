from django.contrib import admin
from django.urls import path
from .views import root_route

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_route, name='root_route'),
]
