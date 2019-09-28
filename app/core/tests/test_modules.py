from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):


    def test_create_user_with_email(self):

        email = 'abcdxyz@gmail.com'
        password = 'abcd123'
        user = get_user_model().objects.create_user(
        email = email,
        password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_create_user_with_normalized_email(self):

        email = 'abcdxyz@GMAIL.COM'
        user = get_user_model().objects.create_user(
        email = email,
        password = 'test123'
        )
        self.assertEqual(user.email, email.lower())

    def test_create_superuser(self):

        email = 'abcdxyzsup@GMAIL.COM'
        user = get_user_model().objects.create_superuser(
        email = email,
        password = 'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)




    def test_create_user_with_valid_email(self):

        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(email = None,
            password = 'test123'
            )
