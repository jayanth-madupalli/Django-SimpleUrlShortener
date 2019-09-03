from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import SusURL, IPStore
from .forms import SubUrlForm
from .utils import get_client_ip
# Create your views here.

def redrView(request, short_code=None):
    obj = get_object_or_404(SusURL, shortcode=short_code)
    ip = get_client_ip(request)
    ipob, created = IPStore.objects.get_or_create(shortcode=short_code, ipaddr=ip)
    ipob.uhits += 1
    obj.hits += 1
    obj.save()
    ipob.save()
    return HttpResponseRedirect(obj.url)

def analyticsView(request, short_code=None):
    ie = SusURL.objects.filter(shortcode=short_code)
    ips = IPStore.objects.filter(shortcode=short_code)
    context = {}
    if ie.exists():
        obj = ie.first()
        if ips.count() == 0:
            context = {
                "obj" : obj,
            }
        else:
            ipo = ips.order_by('-last_accessed')[:5]
            obj.uhits = ips.count()
            context = {
                "obj" : obj,
                "ipo" : ipo,
            }
    return render(request, "stats.html", context)

class HomeView(View):
    def get(self, request):
        form = SubUrlForm()
        context = {
            "form": form,
        }
        return render(request, "home.html", context)
    
    def post(self, request):
        form = SubUrlForm(request.POST)
        context = {}
        if form.is_valid():
            nurl = form.cleaned_data.get('url')
            obj = SusURL.objects.create(url=nurl)
            context = {
                "form": form,
                "obj": obj,

            }
        return render(request, "home.html", context)