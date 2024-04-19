from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=35, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="profiles/images/", default="default.jpg")

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner.username}'s profile"
