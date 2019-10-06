
import sys
import requests
import json


headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQB8dgxwNLy-B0lfPaxMVe4bv5tEkiXQP46YKx8iOPchkx-Tl8Ca7c2kPKoUqUvPfEUCm79yD6Prpzest3Up7JjV9nSLnsPoHyyan6spP-8t_ebArcTEHWHwKkMuwXVf4H-5tlzaAQa8kFHh',
}


params = (
    ('fields', 'items(track(name,artists))'),
    #('limit', 2),
)

response = requests.get('https://api.spotify.com/v1/playlists/6a1lf2JSEHBR9Rax025CdG/tracks', headers=headers, params=params)

data = response.json()
for i in data['items']:
	print (i['track']['name'])
#first task is to list all the playlists from a user
#second task is to list the songs from a playlist link

#third task to convert playlist to youtube

