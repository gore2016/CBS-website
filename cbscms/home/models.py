from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from recent_events.models import AddRecentEvents

# from wagtail.wagtailsearch import index

class HomePage(Page):
	def get_context(self, request):
	        context = super(HomePage, self).get_context(request)
	        context['recent_events_list'] = AddRecentEvents.objects.child_of(self).live().order_by('-first_published_at')
        	return context
	welcome_image = models.FileField(upload_to='events/%Y/%m/%d', blank=True)
	welcome_message_header = models.CharField(max_length=50, blank=True)
	welcome_message = models.CharField(max_length=200, blank = True)
	recents_header = models.CharField(max_length=50, blank = True)
	recents_desc = models.CharField(max_length=200, blank = True)
	content_panels = Page.content_panels + [
	    FieldPanel('welcome_image'),
	    FieldPanel('welcome_message_header'),
	    FieldPanel('welcome_message'),
	    FieldPanel('recents_header'),
	    FieldPanel('recents_desc'),
	]
