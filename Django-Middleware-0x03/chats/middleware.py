import logging
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from django.core.cache import cache

# Configure logging
logging.basicConfig(filename='request_logs.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class RequestLoggingMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the user. If the user is not authenticated, it will be AnonymousUser
        user = request.user if request.user.is_authenticated else 'Anonymous'

        # Log the request information
        logging.info(f"{datetime.now()} - User: {user} - Path: {request.path}")

        response = self.get_response(request)
        return response


class RestrictAccessByTimeMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the current server time
        current_time = datetime.now().time()

        # Define the restricted access hours
        start_time = current_time.replace(hour=9, minute=0, second=0, microsecond=0)
        end_time = current_time.replace(hour=18, minute=0, second=0, microsecond=0)

        # Check if the current time is outside the allowed hours
        if not (start_time <= current_time <= end_time):
            return HttpResponseForbidden("Access to the messaging app is restricted outside of 9 AM and 6 PM.")

        response = self.get_response(request)
        return response
    


class RateLimitMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = 5  # Limit of 5 messages per minute
        self.time_window = 60  # Time window in seconds (1 minute)

    def __call__(self, request):
        if request.method == "POST":
            ip_address = self.get_client_ip(request)
            cache_key = f"rate_limit_{ip_address}"

            # Get the current time
            current_time = datetime.now().time()

            # Get the list of message timestamps from the cache
            message_times = cache.get(cache_key, [])

            # Remove old timestamps outside the time window
            message_times = [t for t in message_times if current_time - t < self.time_window]

            # Check if the number of messages exceeds the limit
            if len(message_times) >= self.rate_limit:
                return HttpResponseForbidden("You have exceeded the message limit. Please try again later.")

            # Add the current message timestamp to the list
            message_times.append(current_time)

            # Update the cache with the new list of message timestamps
            cache.set(cache_key, message_times, self.time_window)

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(',')[0]
        else:
            ip_address = request.META.get('REMOTE_ADDR')
        return ip_address



class RolePermissionMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define the restricted paths (you can customize this based on your needs)
        restricted_paths = ['/admin/', '/host/']

        # Check if the request path is restricted
        if any(request.path.startswith(path) for path in restricted_paths):
            # Check if the user is authenticated and has the required role
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Access denied: You need to be logged in.")

            # Assuming you have a custom user model with a 'role' field
            if request.user.role not in ['admin', 'host']:
                return HttpResponseForbidden("Access denied: You do not have the required permissions.")

        response = self.get_response(request)
        return response