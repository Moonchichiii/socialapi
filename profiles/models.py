from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=255, blank=True, default="")
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profiles/images/', default='default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name if self.display_name else self.user.username

    class Meta:
        ordering = ['-created_at']

    def total_likes(self):
        from posts.models import Post
        return Post.objects.filter(profile=self).aggregate(total_likes=Count('likes'))['total_likes']
