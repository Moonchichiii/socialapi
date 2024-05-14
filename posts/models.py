from django.db import models
from django.contrib.auth import get_user_model
from profiles.models import Profile

User = get_user_model()

class Post(models.Model):
    """Model representing a post."""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    ingredients = models.TextField(max_length=255)
    recipe = models.TextField(max_length=255)
    description = models.TextField(blank=True, max_length=255)
    cooking_time = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/images/', default='posts/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    
    def total_likes(self):
        """Returns the total number of likes for this like instance."""
        return self.likes.count()

    def __str__(self):
        """Returns a string representation of the like."""
        return f"{self.profile.user.username} likes {self.title}"

