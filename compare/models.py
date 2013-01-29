from django.db import models
from django.forms import ModelForm

#Description -> Choice -> Topic

#topic we are comparing
class Topic(models.Model): 
	title = models.CharField(max_length=100)
	desc = models.CharField(max_length=200)
	hits = models.IntegerField()

	#so that when you do CompareGroup.objects.all(), you get [<CompareGroup: "title"]
	def __unicode__(self): 
		return self.title

#choices in each topic
class Choice(models.Model):
	topic = models.ForeignKey(Topic)
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=200)
	likes = models.IntegerField()

	def __unicode__(self):
		return self.title

class Description(models.Model):
	choice = models.ForeignKey(Choice)
	desc = models.CharField(max_length=500)
	likes = models.IntegerField()

	def __unicode__(self):
		return self.desc

class TopicForm(ModelForm):
	class Meta:
		model = Topic