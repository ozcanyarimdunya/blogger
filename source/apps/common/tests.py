from django.test import TestCase

from source.apps.common.models import Contact


class TestContact(TestCase):
    def setUp(self) -> None:
        self.contact = Contact.objects.create(
            name='Test User',
            message='Test message'
        )

    def tearDown(self) -> None:
        Contact.objects.all().delete()

    def test_str(self):
        self.assertEqual(
            str(self.contact),
            'Test User[False]'
        )

    def test_message(self):
        self.assertEqual(
            self.contact.message_,
            'Test message...'
        )
