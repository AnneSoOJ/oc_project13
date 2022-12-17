from django.test import Client, TestCase
from django.urls import reverse

from django.contrib.auth.models import User
from .models import Profile

from pytest_django.asserts import assertTemplateUsed


class TestProfilesindex(TestCase):

    def setUp(self):
        self.client = Client()
        self.path = reverse("profiles:profiles_index")

    def test_when_profiles_index_is_ok_then_return_http200_and_profiles_index_page(self):
        """
        Test to assert if profiles index page is well displayed and returning the right content.
        """
        response = self.client.get(self.path)

        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")

        content = response.content.decode()
        assert "<title>Profiles</title>" in content
        assert "<h1>Profiles</h1>" in content


class TestProfilesDetail(TestCase):

    def setUp(self):
        User.objects.create(
            username="bobdi",
            first_name="Bobby",
            last_name="Diwood",
            email="bobby.diwood@test.com",
        )
        user_test = User.objects.first()
        Profile.objects.create(user=user_test, favorite_city="Test Favorite City")

    def test_when_profile_detail_is_ok_then_return_http200_and_profile_detail_page(self):
        """
        Test to assert if profile detail page is well displayed and returning the right content.
        """
        user_test = User.objects.first()
        self.path = reverse("profiles:profile", args=[user_test.username])
        response = self.client.get(self.path)

        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")

        content = response.content.decode()
        assert f"<title>{user_test.username}</title>" in content
        assert "Back" in content
        assert "Home" in content
        assert "Lettings" in content
