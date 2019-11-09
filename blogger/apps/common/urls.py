from django.urls import path

from .views import IndexView, AboutView, ContactView

app_name = 'common'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
