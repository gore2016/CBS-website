from django.db import models

# from wagtail.wagtailsearch import index
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page



class RecentEventsPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class AddRecentEvents(Page):
    event_date = models.DateField("Post date")
    event_title = models.CharField(max_length=50, blank=True)
    event_description = models.CharField(max_length=250, blank=True)
    event_href_text= models.CharField(max_length=50, blank=True)
    event_href_link = models.CharField(max_length=50, blank=True)
    event_image = models.FileField(upload_to='events/%Y/%m/%d', blank=True)

    # search_fields = Page.search_fields + [
    #     index.SearchField('event_title'),
    #     index.SearchField('event_description'),
    # ]

    content_panels = Page.content_panels + [
        FieldPanel('event_date'),
        FieldPanel('event_title'),
        FieldPanel('event_description'),
        FieldPanel('event_href_text'),
        FieldPanel('event_href_link'),
        FieldPanel('event_image', classname="full"),
    ]