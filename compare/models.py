from django.db import models

#topic we are comparing
class Topic(models.Model): 
	title = models.CharField(max_length=100)
	desc = models.CharField(max_length=200)

	#so that when you do CompareGroup.objects.all(), you get [<CompareGroup: "title"]
	def __unicode__(self): 
		return self.title

#choices in each topic
class Choice(models.Model):
	topic = models.ForeignKey(Topic)
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title