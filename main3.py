import sys
import spotipy
import spotipy.util as util

#first task is to list all the playlists from a user
#second task is to list the songs from a playlist link

#third task to convert playlist to youtube

def show_tracks(tracks):
	for i, item in enumerate(tracks['items']):
		track = item['track']
print


