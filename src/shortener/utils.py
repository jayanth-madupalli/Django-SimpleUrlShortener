import random, string

from django.conf import settings

SCODE_SIZE = getattr(settings, "SCODE_SIZE", 5)

def code_gen(size=SCODE_SIZE, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
	n_code = ''
	for i in range(size):
		n_code += random.choice(chars)
	return n_code

def create_short(instance, size=SCODE_SIZE):
    n_code = code_gen(size=size)
    UClass = instance.__class__
    ie = UClass.objects.filter(shortcode=n_code).exists()
    if ie:
        return create_short(size=size)
    return n_code

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip