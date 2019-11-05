from django.views.generic import TemplateView

from source.apps.article.models import Article


class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all()
        context.update(
            articles=articles
        )
        return context


class AboutView(TemplateView):
    template_name = 'common/about.html'


class ContactView(TemplateView):
    template_name = 'common/contact.html'
