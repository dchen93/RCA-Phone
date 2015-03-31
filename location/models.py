import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Phone(models.Model):
	phone_name = models.CharField(max_length=200)
	updated_time = models.DateTimeField('Time Updated', default=timezone.now())
	def __str__(self):
		return self.phone_name

	# # make updated recently function
	# def was_updated_recently(self):
	# 	return True
	# was_updated_recently.boolean = True
	# was_updated_recently.short_description = 'Updated recently?'


class Center(models.Model):
	phone = models.ForeignKey(Phone)
	center_name = models.CharField(max_length=200)
	current_location = models.BooleanField(default=False)

	def __str__(self):
		return self.center_name