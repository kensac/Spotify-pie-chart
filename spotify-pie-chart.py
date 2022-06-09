#!/usr/bin/env python
# coding: utf-8

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import matplotlib.pyplot as plt

SPOTIPY_CLIENT_ID='ENTER YOUR API CLIENT ID'
SPOTIPY_CLIENT_SECRET='ENTER YOUR API SECRET'
SPOTIPY_REDIRECT_URI='http://127.0.0.1:9090/'
SCOPE = 'user-top-read'


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, scope=SCOPE))

results = sp.current_user_top_tracks(limit=10,time_range='short_term')

counter={}
artists=[]

details=[sp.track(tracks['id']) for tracks in results['items']]
for i in details:
    for j in i['artists']:
        artists.append(j['name'])
        id=j['id']
        result = sp.artist(id)
        for genre in result['genres']:
            if genre in counter:
                counter[genre]+=1
            else:
                counter[genre]=1

graph=plt.pie(counter.values())
plt.legend(counter.keys(),bbox_to_anchor=(1,1,0,0))
plt.show()
