    from django.test import TestCase, Client
    from django.contrib.auth import get_user_model
    from rest_framework.test import APIClient
    from django.urls import reverse
    from rest_framework import status
    from .models import Profile



    class ProfileModelTestCase(TestCase):
        def setUp(self):
            self.user = get_user_model().objects.create_user(username='tester', password='buster2024')
            self.client = APIClient()
            self.client.force_authenticate(user=self.user)
            self.detail_url = reverse('profile-detail', kwargs={'pk': self.user.profile.pk})

        def test_profile_auto_creation(self):
            self.assertTrue(Profile.objects.filter(user=self.user).exists())

        def test_profile_data(self):
            profile = Profile.objects.get(user=self.user)
            self.assertEqual(profile.display_name, self.user.username)
            self.assertTrue(Profile.objects.filter(user=self.user).exists())

        def test_update_display_name(self):
            new_display_name = "New Display Name"
            response = self.client.put(self.detail_url, {'display_name': new_display_name}, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            profile = Profile.objects.get(user=self.user)
            self.assertEqual(profile.display_name, new_display_name)
