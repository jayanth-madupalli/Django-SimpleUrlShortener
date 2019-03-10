from django.core.management.base import BaseCommand, CommandError
from shortener.models import Shorten
class Command(BaseCommand):
    help = 'Refreshes all shortcodes'


    def handle(self, *args, **options):
        return Shorten.objects.ref_shortcodes()