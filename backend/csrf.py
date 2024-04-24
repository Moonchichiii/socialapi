from django.utils.deprecation import MiddlewareMixin
import logging

class DisableCSRFOnJWTAuth(MiddlewareMixin):
    def process_request(self, request):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) > 1 and auth[0].lower() == "bearer":
                setattr(request, '_dont_enforce_csrf_checks', True)
                logging.debug("CSRF checks disabled for this request.")
