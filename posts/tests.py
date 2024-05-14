from django.urls import reverse
from rest_framework import status
from tests.baseuser import BaseUserTestCase
from profiles.models import Profile
from .models import Post

class PostAPITests(BaseUserTestCase):
    def setUp(self):
        super().setUp()
        self.profile, created = Profile.objects.get_or_create(user=self.user)
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
        post_data = {
            'title': 'Post',
            'ingredients': 'Ingredients update',
            'recipe': 'Recipe 2',
            'description': 'Tester Post',
            'cooking_time': 20,
            'profile': self.profile.id
        }
        response = self.client.post(self.create_url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_delete_post(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_like_post(self):
        response = self.client.post(self.like_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.post.likes.count(), 1)

    def test_unlike_post(self):
        self.client.post(self.like_url)
        response = self.client.delete(self.like_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.post.likes.count(), 0)

    def test_liked_posts_list(self):
        self.client.post(self.like_url)
        response = self.client.get(self.liked_posts_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        liked_posts = response.json().get('results', [])
        liked_posts = [post for post in liked_posts if post['id'] == self.post.pk]
        self.assertEqual(len(liked_posts), 1)

    def test_update_post(self):
        new_data = {
            'title': 'Updated Title',
            'description': 'Updated Description'
        }
        response = self.client.patch(self.detail_url, new_data, format='json')
        self.post.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.post.title, 'Updated Title')
        self.assertEqual(self.post.description, 'Updated Description')

