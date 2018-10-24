from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from recent_events.models import AddRecentEvents

# from wagtail.wagtailsearch import index

class HomePage(Page):
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['recent_events_list'] = AddRecentEvents.objects.child_of(self).live()
        return context
