from django.contrib.auth import get_user_model
from rest_framework import status
from profiles.models import Profile
from followers.models import Follower
from tests.baseuser import BaseUserTestCase

User = get_user_model()

class FollowersAPITest(BaseUserTestCase):
    def setUp(self):
        super().setUp()

        # Second user and profile
        self.user2 = User.objects.create_user(
            username='buster2',
            email='butser2@gmail.com',
            password='gmail@busters2'
        )
        self.profile2 = Profile.objects.get_or_create(user=self.user2)[0]

        # URLs for following and unfollowing
        self.follow_url = '/follow-profile/'
        self.unfollow_url = '/unfollow-profile/'

    def test_follow_profile(self):
        """Test following a profile."""
        response = self.client.post(self.follow_url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follower.objects.count(), 1)
        self.assertEqual(Follower.objects.get().user, self.profile)
        print("Test 'test_follow_profile' completed.")

    def test_unfollow_profile(self):        
        # First, follow the profile
        self.client.post(self.follow_url)
        self.assertEqual(Follower.objects.count(), 1)

        # Then, unfollow the profile
        response = self.client.delete(self.unfollow_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Follower.objects.count(), 0)
        print("Test 'test_unfollow_profile' completed.")

    def tearDown(self):
        Follower.objects.all().delete()
        self.user2.delete()
        super().tearDown()