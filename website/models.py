from __future__ import unicode_literals
from django.db import models

# Create your models here
class data(models.Model):

	temperature = models.IntegerField()
	humidity = models.IntegerField()
	co2 = models.IntegerField()
	smoke = models.IntegerField()
	latitude = models.FloatField()
	longitude = models.FloatField()

	def __str__(self):
		return str(self.latitude + " - " + self.longitude)