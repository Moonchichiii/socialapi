from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile

class Follower(models.Model):
    """
    Model representing a follower relationship between a user and a profile.
    The user who is following the profile.
    The profile being followed by the user.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follower_set')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'profile')

    def __str__(self):        
        return f'{self.user.username} follows {self.profile.display_name}'
