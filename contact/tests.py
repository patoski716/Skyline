from django.test import TestCase
from .models import Contact


class ContactViewTests(TestCase):
    def test_viewcontact_returns_contact_list(self):
        Contact.objects.create(
            name="Ada Lovelace",
            phone="123456789",
            email="ada@example.com",
            message="Hello",
        )

        response = self.client.get("/api/v1/viewcontact/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["name"], "Ada Lovelace")
