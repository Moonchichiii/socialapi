from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

class ProfileModelTestCase(TestCase):
    def setUp(self):
        self.test_user = get_user_model().objects.create_user(username="testuser", password="testpassword")

    def test_profile_auto_creation(self):
        profile_exists = Profile.objects.filter(user=self.test_user).exists()
        self.assertTrue(profile_exists)

    def test_profile_data(self):
        profile = Profile.objects.get(user=self.test_user)
        self.assertEqual(profile.display_name, self.test_user.username)
        self.assertTrue(profile.image.name.endswith('default.png'))

    