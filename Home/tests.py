from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class HomeTemplateAuthenticationTests(TestCase):
    def test_logged_out_homepage_keeps_cta_links_separate(self):
        response = self.client.get(reverse("home"))
        content = response.content.decode()

        primary_start = content.index('<a href="/login/" class="primary-btn">')
        secondary_start = content.index('<a href="/register/" class="secondary-btn">')

        self.assertLess(content.index("</a>", primary_start), secondary_start)

    def test_logged_in_homepage_keeps_cta_and_logout_links_separate(self):
        user = User.objects.create_user(username="home-test-user", password="password")
        self.client.force_login(user)

        response = self.client.get(reverse("home"))
        content = response.content.decode()

        primary_start = content.index(
            f'<a href="{reverse("recepie")}" class="primary-btn">'
        )
        secondary_start = content.index('<a href="/register/" class="secondary-btn">')
        logout_start = content.index('<a href="/logout/" class="logout-btn">')

        self.assertLess(content.index("</a>", primary_start), secondary_start)
        self.assertLess(content.index("</a>", logout_start), content.index("</nav>"))
