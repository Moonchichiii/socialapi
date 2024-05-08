from django.db import models
from django.contrib.auth.models import User

from profiles.models import Profile


# Create your models here.


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    recipe = models.TextField()
    description = models.TextField(blank=True)
    cooking_time = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/images/', default='posts/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.profile.user.username}"


class Like(models.Model):
    post = models.ForeignKey('Post', related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"