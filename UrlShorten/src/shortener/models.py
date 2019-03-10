from django.conf import settings
from django.db import models

from .utils import code_gen, create_shortcode
from .validators import validate_url

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class ShortenUrlManager(models.Manager):
    def all(self,*args,**kwargs):
        qs =super(ShortenUrlManager,self).all(*args,**kwargs)
        qs = qs.filter(active=True)
        return qs

    def ref_shortcodes(self):
        qs = Shorten.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes +=1
        return "New Codes made: {i}".format(i=new_codes)

# Create your models here.
class Shorten(models.Model):
    url = models.CharField(max_length=220, validators = [validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    objects= ShortenUrlManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(Shorten,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        return "http://www.short:8000/{shortcode}".format(shortcode=self.shortcode)