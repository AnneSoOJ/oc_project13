from django.test import Client, TestCase
from django.urls import reverse

from .models import Address, Letting

from pytest_django.asserts import assertTemplateUsed


class TestLettingsIndex(TestCase):

    def setUp(self):
        self.client = Client()
        self.path = reverse("lettings:lettings_index")

    def test_when_lettings_index_is_ok_then_return_http200_and_lettings_index_page(self):
        """
        Test to assert if lettings index page is well displayed and returning the right content.
        """
        response = self.client.get(self.path)

        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")

        content = response.content.decode()
        assert "<title>Lettings</title>" in content
        assert "<h1>Lettings</h1>" in content


class TestLettingsDetail(TestCase):

    def setUp(self):
        Address.objects.create(
            number=1234,
            street="Test street",
            city="Test city",
            state="AA",
            zip_code=00000,
            country_iso_code="AAA",
        )
        address_test = Address.objects.first()
        Letting.objects.create(title="Test Title", address=address_test)

    def test_when_letting_detail_is_ok_then_return_http200_and_letting_detail_page(self):
        """
        Test to assert if one letting detail page is well displayed and returning the right content.
        """
        letting_test = Letting.objects.first()
        self.path = reverse("lettings:letting", args=[letting_test.id])
        response = self.client.get(self.path)

        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")

        content = response.content.decode()
        assert f"<title>{letting_test.title}</title>" in content
        assert "Back" in content
        assert "Home" in content
        assert "Profiles" in content
