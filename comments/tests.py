from tests.baseuser import BaseUserTestCase
from django.urls import reverse
from rest_framework import status
from profiles.models import Profile
from posts.models import Post
from .models import Comment

class CommentTestCase(BaseUserTestCase):
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
        self.comment = Comment.objects.create(
            profile=self.profile,
            post=self.post,
            text='This is a comment'
        )
        self.list_url = reverse('comment-list', kwargs={'post_id': self.post.pk})
        self.detail_url = reverse('comment-detail', kwargs={'post_id': self.post.pk, 'pk': self.comment.pk})

    def test_create_comment(self):
        comment_data = {'text': 'New comment'}
        response = self.client.post(self.list_url, comment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)

    def test_delete_comment(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)

    def test_update_comment(self):
        new_data = {'text': 'Updated comment'}
        response = self.client.patch(self.detail_url, new_data, format='json')
        self.comment.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.comment.text, 'Updated comment')

    def test_get_comments(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
