from datetime import datetime

from django.test import TestCase

from blogger.apps.common.models import Contact, Stats


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
            'Test User/False'
        )

    def test_message(self):
        self.assertEqual(
            self.contact.message_,
            'Test message...'
        )


class TestStats(TestCase):
    def tearDown(self) -> None:
        Stats.objects.all().delete()

    def test_str(self):
        stats = Stats.objects.create(path='/hello/')
        self.assertEqual(str(stats), '/hello/')

    def test_stats(self):
        self.client.get('/about/')
        self.client.get('/about/')
        self.client.get('/contact/')
        self.client.get('/contact/')
        self.client.get('/contact/')
        self.client.get('/contact/')
        self.client.get('/')
        self.client.get('/admin/')

        self.assertEqual(
            Stats.objects.all().count(), 3
        )
        self.assertEqual(
            Stats.objects.get(path='/contact/').views, 4
        )

    def test_last_viewed(self):
        self.client.get('/contact/')
        self.client.get('/contact/')
        self.client.get('/')
        self.client.get('/about/')
        self.client.get('/')
        self.client.get('/about/')
        self.client.get('/about/')
        self.client.get('/contact/')
        stat = Stats.objects.get(path='/contact/')
        self.assertAlmostEqual(
            stat.last_viewed.minute, datetime.now().minute
        )
        self.assertNotEqual(
            stat.last_viewed.time(), stat.created.time()
        )

    def test_visit_url(self):
        self.client.get('/contact/')
        stat = Stats.objects.get(path='/contact/')
        self.assertInHTML(
            '<a class="button" href="/contact/" target="blank">Link</a>',
            stat.visit,
        )


class TestContactView(TestCase):
    def tearDown(self) -> None:
        Contact.objects.all().delete()

    def test_contact_remote(self):
        payload = {
            'name': 'Test user',
            'email': 'test@email.com',
            'message': 'Test message',
        }
        response = self.client.post('/contact/', data=payload, REMOTE_ADDR="127.0.0.1")
        self.assertEqual(response.status_code, 302)

    def test_contact_forwarded(self):
        payload = {
            'name': 'Test user',
            'email': 'test@email.com',
            'message': 'Test message',
        }
        response = self.client.post('/contact/', data=payload, HTTP_X_FORWARDED_FOR="10.0.0.1")
        self.assertEqual(response.status_code, 302)
