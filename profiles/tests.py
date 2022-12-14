from django.test import Client, TestCase
from django.urls import reverse


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

        assert b"<title>Profiles</title>"
        assert b"<h1>Profiles</h1>"
