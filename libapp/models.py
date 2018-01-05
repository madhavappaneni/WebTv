from django.db import models

class PostModel(models.Model):
	title = models.TextField(null=True, blank=True)
	