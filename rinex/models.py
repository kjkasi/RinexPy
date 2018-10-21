# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Station(models.Model):
	#lon = models.FloatField()
	#lat = models.FloatField()
	x = models.FloatField(default=0.0)
	y = models.FloatField(default=0.0)
	z = models.FloatField(default=0.0)
	name = models.CharField(max_length=255)
	code = models.CharField(max_length=10, unique=True)
	def __str__(self):
		return self.name + '(' +  self.code  + ')'
	
class SatelliteSystem(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name
		
'''
1) python manage.py makemigrations
2) python manage.py migrate
3) python manage.py runserver
'''