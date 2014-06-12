from django.db import models

import mptt


class MenuRuURLs(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField(max_length=200)

	def __unicode__(self):
		return self.title
