from django.test import TestCase
from django.contrib.auth import get_user_model
from unittest.mock import patch

from core import models


class ModelTests(TestCase):
    """Test the core models"""

    def test_create_user_with_email(self):
        """Create User with email"""
        email = "abhinavchavali12@gmail.com"
        password = "Abhinav!23"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_normalize_email(self):
        """Normalize user email"""
        email = "abhinavchavali34@GmAiL.cOm"
        user = get_user_model().objects.create_user(email=email, password='URAGAY')
        self.assertEqual(user.email, email.lower())

    def test_user_invalid_email(self):
        """Test user invalid email"""
        password = "Abhinav!23"
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, password)

    def test_create_new_super_user(self):
        """create new super user"""
        email = "abhinavchavali12@gmail.com"
        password = "Abhinav!23"
        user = get_user_model().objects.create_superuser(email=email, password=password)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
