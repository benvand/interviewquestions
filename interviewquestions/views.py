# Create your views here.
#Below imports negated by render shortcut method

from django.shortcuts import render

from django.conf import settings
from django.contrib.sites.models import get_current_site

def comingSoon(request):
    Site = get_current_site(request)
    context = {'global_site':Site,}
    return render(request, 'comingsoon.html', context)

def fiveHundred(request):
    return render(request, '500.html')

def fourHundred(request):
    return render(request, '400.html')