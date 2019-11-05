from django.views.generic import TemplateView, ListView

from source.apps.article.models import Article


class IndexView(ListView):
    template_name = 'common/index.html'
    queryset = Article.objects.all()
    paginate_by = 4


class AboutView(TemplateView):
    template_name = 'common/about.html'


class ContactView(TemplateView):
    template_name = 'common/contact.html'
