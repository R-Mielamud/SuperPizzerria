from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout
import time as t

class LogoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        time = request.session.get("time")

        if not time:
            request.session["time"] = t.time()
        elif t.time() - time > 60:
            logout(request)
        else:
            request.session["time"] = t.time()

    def process_response(self, request, response):
        return response
