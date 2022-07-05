from django.db import models
from django.conf import settings

from .utils import create_short
# Create your models here.

DOMAIN = getattr(settings, "DOMAIN", "http://localhost:8000/")

class SusURL(models.Model):
	url = models.CharField(max_length=500, )
	shortcode = models.CharField(max_length=16, unique=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, null=True)
	hits = models.IntegerField(default=0)
	active = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		super(SusURL, self).save(*args, **kwargs)
		self.update_model()
	
	def update_model(self):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_short(self)
			self.save()

	def get_short_url(self):
		return DOMAIN+"{shortcode}".format(shortcode=self.shortcode)


class IPStore(models.Model):
	shortcode = models.CharField(max_length=16, unique=True)
	ipaddr = models.CharField(max_length=12, null=True)
	last_accessed = models.DateTimeField(auto_now=True, null=True)
	uhits = models.IntegerField(default=0)