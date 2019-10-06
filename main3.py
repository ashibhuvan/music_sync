import sys
import spotipy
import spotipy.util as util

#first task is to list all the playlists from a user

#secondt basic task is too list all the songs from a playist


def show_tracks(tracks):
	for i, item in enumerate(tracks['items']):
		track = item['track']
print


