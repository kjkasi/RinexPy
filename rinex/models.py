# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Place(models.Model):
	lon = models.FloatField()
	lat = models.FloatField()
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name
	
class SatelliteSystem(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name