from django.test import TestCase
from .serializers import RegistrationSerializer

class RegistrationSerializerTestCase(TestCase):
    def test_serializer_with_valid_data(self):
        valid_data = {
            'username': 'myuser',
            'email': 'user@example.com',
            'password1': 'mypassword123',
            'password2': 'mypassword123'
        }
        serializer = RegistrationSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'myuser')
        self.assertTrue(user.check_password('mypassword123'))

    def test_serializer_with_invalid_data_password_mismatch(self):
        invalid_data = {
            'username': 'myuser',
            'email': 'user@example.com',
            'password1': 'mypassword123',
            'password2': 'wrongpassword123'
        }
        serializer = RegistrationSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        
