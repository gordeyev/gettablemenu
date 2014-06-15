from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class MenuRuURLs(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField(max_length=200)

	def __unicode__(self):
		return self.title


class Food(models.Model):
	name = models.CharField(max_length=200)
	weight = models.FloatField(null=True)
	cost = models.FloatField(null=True)

	def __unicode__(self):
		return self.name


class RestoMenu(MPTTModel):
	level = models.IntegerField()
	name = models.CharField(max_length=200, null=True)
	food = models.FloatField(Food, null=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

	def __unicode__(self):
		return self.name


class Resto(models.Model):
	name = models.CharField(max_length=200)
	url = models.URLField(max_length=200, null=True)
	gettable_id = models.IntegerField(null=True)
	x = models.FloatField(null=True)
	y = models.FloatField(null=True)
	menu = models.ForeignKey(RestoMenu, null=True)

	def __unicode__(self):
		return self.name
