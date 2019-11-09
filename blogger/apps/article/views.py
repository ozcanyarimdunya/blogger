from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from .models import Article


class ArticleDetail(DetailView):
    queryset = Article.objects.published()
    template_name = 'article/detail.html'


class PreviewDetail(LoginRequiredMixin, ArticleDetail):
    queryset = Article.objects.all()
