from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AuthenticationRedirectTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test-user',
            password='test-password-123',
        )

    def test_valid_login_logs_user_in_and_redirects_to_recepie(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'test-user', 'password': 'test-password-123'},
        )

        self.assertRedirects(response, reverse('recepie'), fetch_redirect_response=False)
        self.assertEqual(
            str(self.client.session['_auth_user_id']),
            str(self.user.pk),
        )

    def test_invalid_login_redirects_back_with_message(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'test-user', 'password': 'wrong-password'},
            follow=True,
        )

        self.assertRedirects(response, reverse('login'))
        self.assertContains(response, 'Invalid username or password')

    def test_registration_redirects_to_login_with_message(self):
        response = self.client.post(
            reverse('register'),
            {
                'username': 'new-user',
                'email': 'new-user@example.com',
                'password': 'new-password-123',
            },
            follow=True,
        )

        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='new-user').exists())
        self.assertContains(response, 'Account created successfully')
