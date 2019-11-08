from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings

from source.apps.article.models import Article, Stats

User = get_user_model()


@override_settings(MEDIA_ROOT='/tmp')
class TestArticle(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='admin', password='123')
        self.article = Article.objects.create(
            author=self.user,
            title='test title',
            subtitle='test subtitle',
            content='test content',
            image='test image',
        )

    def tearDown(self) -> None:
        Article.objects.all().delete()
        User.objects.all().delete()

    def test_str(self):
        self.assertEqual(
            str(self.article),
            'test title'
        )

    def test_slug(self):
        self.assertEqual(
            self.article.slug,
            'test-title'
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.article.get_absolute_url(),
            '/article/test-title/'
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
