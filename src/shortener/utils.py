import random, string

from django.conf import settings

b62_map = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def code_gen(id):
    n_code = ''
    while id > 0:
        n_code += b62_map[id % 62]
        id //= 62
    return n_code

def create_short(instance):
    n_code = code_gen(id=instance.id)
    return n_code

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip