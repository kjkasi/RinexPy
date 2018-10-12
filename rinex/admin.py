# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Place, SatelliteSystem

admin.site.register(Place)
admin.site.register(SatelliteSystem)
