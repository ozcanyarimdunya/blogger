from django.urls import path

from .views import ArticleDetail

app_name = 'article'
urlpatterns = [
    path('<str:slug>/', ArticleDetail.as_view(), name='detail'),
]
