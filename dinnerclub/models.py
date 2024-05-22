from django.db import models
from profiles.models import Profile

# Create your models here.
ALLERGY_CHOICES = [
    ('none', 'None'),
    ('gluten', 'Gluten'),
    ('milk', 'Milk'),
    ('eggs', 'Eggs'),
    ('peanuts', 'Peanuts'),
    ('soybeans', 'Soybeans'),
    ('fish', 'Fish'),
    ('crustaceans', 'Crustaceans'),
    ('molluscs', 'Molluscs'),
    ('celery', 'Celery'),
    ('lupin', 'Lupin'),
    ('sesame', 'Sesame'),
    ('mustard', 'Mustard'),
    ('sulphites', 'Sulphites'),
]

class DinnerClub(models.Model):
    host = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hosted_events')
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=150)
    date_time = models.DateTimeField()
    theme_dinner = models.CharField(max_length=100, blank=True)
    allergies = models.CharField(max_length=500, blank=True)
    type_of_dinner = models.CharField(max_length=100, blank=True)
    invited_profiles = models.ManyToManyField(Profile, related_name='invited_events')
    participants = models.ManyToManyField(Profile, related_name='participating_events', blank=True)

    def __str__(self):
        return f"{self.title} by {self.host}"

    def get_allergies_list(self):
        return self.allergies.split(',')

    def set_allergies_list(self, allergies):
        self.allergies = ','.join(allergies)
