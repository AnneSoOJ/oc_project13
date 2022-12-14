from django.test import Client, TestCase
from django.urls import reverse


class TestHomeIndex(TestCase):

    def setUp(self):
        self.client = Client()
        self.path = reverse("home")

    def test_when_home_index_is_ok_then_return_http200_and_home_index_page(self):
        """
        Test to assert if index page is well displayed and returning the right content.
        """
        response = self.client.get(self.path)

        assert response.status_code == 200

        assert b"<title>Holiday Homes</title>"
        assert b"<h1>Welcome to Holiday Homes</h1>"
