from __future__ import unicode_literals
from django.db import models

class PostModel(models.Model):
	title = models.CharField(null=True, blank=True, max_length=100)
