from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileModelTestCase(TestCase):
    """
    Test cases for the Profile model.
    """
    def setUp(self):
        # Create a test user
        self.test_user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        # Profile of the test user
        self.profile = Profile.objects.create(
            owner=self.test_user,
            name="Tester2024",
            content="content's",
            image="default.jpg"
        )

    def test_profile_creation(self):
        expected_name = "Tester2024"
        self.assertEqual(
            self.profile.name,
            expected_name,
            f"Profile name to be {expected_name}, {self.profile.name}."
        )

    def test_profile_image_default(self):
        self.assertIn("default.jpg", self.profile.image.name)

    def test_profile_string_representation(self):
        
        self.assertEqual(
            str(self.profile),
            f"{self.test_user.username}'s profile"
        )
