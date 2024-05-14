from tests.baseuser import BaseUserTestCase
from django.urls import reverse
from rest_framework import status
from .models import Profile


class ProfileModelTestCase(BaseUserTestCase):
    def setUp(self):
        super().setUp()
        self.detail_url = reverse('profile-detail', kwargs={'pk': self.user.profile.pk})

    def test_profile_auto_creation(self):
        """
        creating a profile for each new user
        """
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_profile_data(self):
        """Check that the profile data matches the expected initial settings."""
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.display_name, self.user.username)
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_update_display_name(self):
        """
        updating the display name
        """
        new_display_name = "New Display Name"
        response = self.client.put(self.detail_url, {'display_name': new_display_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.display_name, new_display_name)
