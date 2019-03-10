from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent
from .forms import SubUrlForm
from .models import Shorten

class URLRedrView(View):
    def get(self,request,shortcode=None,*args,**kwargs):
        obj = get_object_or_404(Shorten, shortcode=shortcode)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
    def post(self, request, *args, **kwargs):
        return HttpResponse()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        t_form = SubUrlForm()
        context = {
            "title": "Urrl",
            "form": t_form
        }
        return render(request, "shortener/home.html", context)
    
    def post(self, request, *args, **kwargs):
        form = SubUrlForm(request.POST)
        context = {}
        if form.is_valid():
            nurl = form.cleaned_data.get('url')
            obj = Shorten.objects.filter(url=nurl).first()
            if  obj == None :
                obj = Shorten.objects.create(url=nurl)
            else:
                obj.aexists = True
            print(form.cleaned_data)
            if nurl != "":
                context = {
                    "title": "Shortened Url",
                    "form": form,
                    "obj": obj,
                }
        return render(request, "shortener/home.html", context)

class StatsView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = Shorten.objects.filter(shortcode=shortcode).first()
        context = {
            "obj" : obj
        }
        print(shortcode)
        return render(request, "shortener/stats.html", context)

def sh_redr_view(request, shortcode=None, *args, **kwargs):

    """
    qs=Shorten.objects.filter(shortcode__iexact = shortcode.upper())
    if(qs.exists() and qs.count() == 1):
        obj= qs.first()
        obj_url=obj.url
    """
    print(shortcode)
    obj = get_object_or_404(Shorten, shortcode=shortcode)
    obj_url = obj.url
    return HttpResponseRedirect(obj_url)
