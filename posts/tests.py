from django.urls import reverse
from rest_framework import status
from tests.baseuser import BaseUserTestCase
from profiles.models import Profile
from .models import Post

class PostAPITests(BaseUserTestCase):
    
    def setUp(self):
        """
        Test cases for the Post API.
        """

        super().setUp()
        self.profile = getattr(self.user, 'profile', None) or Profile.objects.create(user=self.user)
        self.post = Post.objects.create(
            profile=self.profile,
            title='Title',
            ingredients='Ingredients',
            recipe='Recipe',
            description='Description',
            cooking_time=10
        )
        self.create_url = reverse('post-list')
        self.detail_url = reverse('post-detail', kwargs={'pk': self.post.pk})
        self.like_url = reverse('toggle-like', kwargs={'post_id': self.post.pk})
        self.liked_posts_url = reverse('liked-posts')

    def test_create_post(self):
        """
        Creating a new post.
        """
        post_data = {
            'title': 'Post',
            'ingredients': 'Ingredients update',
            'recipe': 'Recipe 2',
            'description': 'Tester Post',
            'cooking_time': 20,
            'profile': self.profile.id
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.create_url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_delete_post(self):
        """
        Deleting a post.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
          
        

    def test_update_post(self):
        """
        Test updating a post.
        """
        new_data = {
            'title': 'Updated Title',
            'description': 'Updated Description'
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(self.detail_url, new_data, format='json')
        self.post.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.post.title, 'Updated Title')
        self.assertEqual(self.post.description, 'Updated Description')
