from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Represents a user profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=255, blank=True, default="")
    image = models.ImageField(upload_to='profiles/images/', default='default.png')
    bio = models.TextField(blank=True, verbose_name="Biography")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta class for Profile model.
        """
        ordering = ['-created_at']

        def __str__(self):
            return f"{self.user.get_username()}'s Profile"
