from django.urls import path

from .views import IndexView

app_name = 'common'
urlpatterns = [
    path('', IndexView.as_view()),
]
