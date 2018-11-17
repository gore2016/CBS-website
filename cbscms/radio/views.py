from django.shortcuts import render
from django.db import connections

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def upcoming_refresh(request):
	with connections['users'].cursor() as cursor:
        	cursor.execute("SELECT songs.ID, songs.artist as artist, songs.title as title, queuelist.songID FROM songs, queuelist WHERE songs.song_type=0 AND songs.ID=queuelist.songID LIMIT 3;")
        	upcoming = dictfetchall(cursor)
	return render(request, 'radio/upcoming_refresh.html', {
	    'upcoming': upcoming,
	})

def playing_refresh(request):
	with connections['users'].cursor() as cursor:
		cursor.execute("SELECT artist, title, date_played FROM history WHERE song_type=0 ORDER BY date_played DESC LIMIT 1;")
		now_playing = cursor.fetchone()
	return render(request, 'radio/playing_refresh.html', {
	    'now_playing': now_playing,
	})
