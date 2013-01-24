from django.db import models

class CompareGroup(models.Model):
	desc = models.CharField(max_length=200)

	def __unicode__(self):
		return self.desc

class CompareItem(models.Model):
	compareGroup = models.ForeignKey(CompareGroup)
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title