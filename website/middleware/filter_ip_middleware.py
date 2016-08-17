from django.http import HttpResponseForbidden
from django.http import Http404
from django.utils.deprecation import MiddlewareMixin

class FilterIPMiddleware(MiddlewareMixin):
    # Check if client IP is allowed
    def process_request(self, request):
        print "*"*50
        print "*"*50
        print "printing the request"
        print
        print
        print request
        print
        print
        print request.META.get('REMOTE_ADDR')
        print
        print
        allowed_ips = []#['192.168.1.1', '123.123.123.123',] # Authorized ip's
        ip = request.META.get('REMOTE_ADDR') # Get client IP
        if ip not in allowed_ips:
            print "raising the 404 since ip is not allowed"
            raise Http404("ip address not allowed") # If user is not allowed raise Error

        print "after exception"
       # If IP is allowed we don't do anything
        return None