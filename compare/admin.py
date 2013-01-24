from compare.models import Topic
from compare.models import Choice
from django.contrib import admin

#admin.site.register(Topic)


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class TopicAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['title']}),
		(None, 				 {'fields': ['desc']}),
	]
	inlines = [ChoiceInline]
	search_fields = ['title']

admin.site.register(Topic, TopicAdmin)