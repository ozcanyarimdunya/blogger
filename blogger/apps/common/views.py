from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView

from blogger.apps.article.models import Article
from .forms import ContactForm


class IndexView(ListView):
    template_name = 'common/index.html'
    queryset = Article.objects.published()
    paginate_by = 4


class AboutView(TemplateView):
    template_name = 'common/about.html'


class ContactView(FormView):
    template_name = 'common/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.ip = self.visitor_ip_address
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, message='Thank you for message! I will get back to you as soon as possible!')
        return reverse_lazy('common:contact')

    @property
    def visitor_ip_address(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip
