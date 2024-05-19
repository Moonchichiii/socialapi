from django.contrib import admin
from .models import Follower

class FollowerAdmin(admin.ModelAdmin):
    list_display = ('profile', 'created_at')    
    list_filter = ('created_at',)

admin.site.register(Follower, FollowerAdmin)
