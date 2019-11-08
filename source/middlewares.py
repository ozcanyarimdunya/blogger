from django.utils.deprecation import MiddlewareMixin

from source.apps.article.models import Stats


class StatsMiddleWare(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        if not request.path.startswith('/admin/'):
            obj, created = Stats.objects.get_or_create(path=request.path)
            obj.views += 1
            obj.save()
