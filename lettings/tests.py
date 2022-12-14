from django.test import Client, TestCase
from django.urls import reverse


class TestLettingsindex(TestCase):

    def setUp(self):
        self.client = Client()
        self.path = reverse("lettings:lettings_index")

    def test_when_lettings_index_is_ok_then_return_http200_and_lettings_index_page(self):
        """
        Test to assert if lettings index page is well displayed and returning the right content.
        """
        response = self.client.get(self.path)

        assert response.status_code == 200

        assert b"<title>Lettings</title>"
        assert b"<h1>Lettings</h1>"
