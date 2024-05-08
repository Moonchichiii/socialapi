from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

class BaseUserTestCase(TestCase):
    """
    BaseUser for tests
    """

    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user(username='tester2024', email='tester2024@gmail.com', password='buster2024')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def tearDown(self):
        self.user.delete()
