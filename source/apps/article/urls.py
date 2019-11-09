from django.urls import path

from .views import ArticleDetail, PreviewDetail

app_name = 'article'
urlpatterns = [
    path('<str:slug>/', ArticleDetail.as_view(), name='detail'),
    path('preview/<str:slug>/', PreviewDetail.as_view(), name='preview'),
]
