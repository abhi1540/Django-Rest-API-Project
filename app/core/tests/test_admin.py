from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """this will execute before any test cases runs. """

        self.client = Client()
        email = 'abcdxyzsup@GMAIL.COM'
        self.admin_user = get_user_model().objects.create_superuser(
                          email=email, password="mypwd123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
                    email="abctext@gmail.com", password="mypwdtest123",
                    name="test user name"
        )

    def test_user_listed(self):

        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        # this will get the user details
        # assertContains does status 200 test and then find parameters
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_chnagelist(self):
        """Test that user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
