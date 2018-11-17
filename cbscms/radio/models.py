from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
#from django.db import connection
from django.db import connections
from recent_events.models import AddRecentEvents

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

class RadioPage(Page):
	def get_context(self,request):
		context = super(RadioPage, self).get_context(request)
		with connections['users'].cursor() as cursor:
			cursor.execute("SELECT songs.ID, songs.artist as artist, songs.title as title, queuelist.songID FROM songs, queuelist WHERE songs.song_type=0 AND songs.ID=queuelist.songID LIMIT 3;")
			context['upcoming'] = dictfetchall(cursor)
			cursor.execute("SELECT artist, title, date_played FROM history WHERE song_type=0 ORDER BY date_played DESC LIMIT 1;")
			context['now_playing'] = cursor.fetchone()
		return context
	parallax_image = models.FileField(upload_to='events/%Y/%m/%d', blank=True)
	content_panels = Page.content_panels + [
		FieldPanel('parallax_image'),
	]
