from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from profiles.models import Profile
from followers.models import Follower

User = get_user_model()

class FollowersAPITest(TestCase):
    """
    Test case for the Followers API.
    """

    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(username='buster1', email='buster1@gmail.com', password='gmail@busters1')
        self.profile1 = Profile.objects.get_or_create(user=self.user1)[0]
        self.user2 = User.objects.create_user(username='buster2', email='buster2@gmail.com', password='gmail@busters2')
        self.profile2 = Profile.objects.get_or_create(user=self.user2)[0]
        self.follow_url = reverse('follower-list-create')
        self.unfollow_url = reverse('follower-detail', kwargs={'pk': self.profile2.id})

    def test_follow_profile(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(self.follow_url, {'profile_id': self.profile2.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(Follower.objects.count(), 1)
        self.assertEqual(Follower.objects.get().follower, self.profile1)
        self.assertEqual(Follower.objects.get().profile, self.profile2)

    def test_unfollow_profile(self):
        self.client.force_authenticate(user=self.user1)
        self.client.post(self.follow_url, {'profile_id': self.profile2.id})
        self.assertEqual(Follower.objects.count(), 1)
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(self.unfollow_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.data)
        self.assertEqual(Follower.objects.count(), 0)

    def tearDown(self):
        Follower.objects.all().delete()
        self.user1.delete()
        self.user2.delete()
