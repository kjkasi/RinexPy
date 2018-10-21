# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Station, SatelliteSystem

def index(request):
    all_objects = SatelliteSystem.objects.all()
    template = loader.get_template('rinex/index.html')
    context = {
        'latest_place_list': all_objects,
    }
    return HttpResponse(template.render(context, request))
	
def bootstrap(request):
	return render(request, 'rinex/bootstrap.html')