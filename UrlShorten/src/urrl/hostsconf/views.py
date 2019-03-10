from django.conf import settings
from django.http import HttpResponseRedirect

DEFAULT_REDR_URL = getattr(settings, "DEFAULT_REDR_URL", "http://localhost:8000")

def wildcard_redirect(request, path=None):
    new_url = DEFAULT_REDR_URL
    if path is not None:
        new_url = DEFAULT_REDR_URL + "/" + path
    return HttpResponseRedirect(new_url)