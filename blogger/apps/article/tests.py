from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings

from blogger.apps.article.models import Article

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

    def test_preview_url(self):
        self.assertInHTML(
            '<a class="button" href="/article/preview/test-title/" target="blank">Preview</a>',
            self.article.preview,
        )
