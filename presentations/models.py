from __future__ import unicode_literals
from django.db import models

class PostModel(models.Model):
	title = models.CharField(null=True, blank=True, max_length=100)
	place = models.CharField(null=True, blank=True, max_length=100)
	date = models.DateTimeField()

	def __unicode__(self):
		return str(self.title)+" at "+str(self.place)+"on "+str(self.date.strftime("%H:%M, %A, %d %B %Y."))
