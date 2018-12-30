from log.models import Log
from django.utils.deprecation import MiddlewareMixin

class LogMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path
        method = request.method
        client_ip = request.META['REMOTE_ADDR']
        if method == 'GET':
            query = request.GET.urlencode()
        elif method == 'POST':
            query = request.POST.copy().urlencode()
        else:
            query = ''
        Log(
            path = path,
            method = method,
            client_ip = client_ip,
            query = query
        ).save()
        return None