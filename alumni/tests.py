from django.test import TestCase

# Create your tests here.

import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Chorus, Member, unapprovedMember
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class LoginTests(TestCase):

    mock_username_one = 'fake@example.com'
    mock_password_one = 'password'

    def test_can_login(self):
        mock_user = self.create_mock_user(self.mock_username_one, self.mock_password_one)
        user = authenticate(username=self.mock_username_one, password=self.mock_password_one)

        self.assertNotEqual(user, None)

        self.delete_mock_user(mock_user.id)

    def create_mock_user(self, email, password):
        user = User()
        user.username = email
        user.email = email
        user.set_password(password)
        user.save()
        return user

    def delete_mock_user(self, user_id):
        User.objects.filter(id=user_id).delete()