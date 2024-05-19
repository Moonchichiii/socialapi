from django.db import models
from profiles.models import Profile

class Follower(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('profile', 'follower')

    def __str__(self):
        return f'{self.follower.display_name} follows {self.profile.display_name}'
