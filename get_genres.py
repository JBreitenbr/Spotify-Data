from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
import spotipy
import pandas as pd
import random
import math
client_id = "12308f6c7b9c4194a6ca9e06f43d3bfd"
client_secret = "e27a673a043147df8bf4a5d0a9fe8084"
#scope = "user-library-read"
username = "31nfsp7vapk4zh24xzvw3lkavx5e"
redirect_uri = 'https://juliascodingeckle.pythonanywhere.com/spoti/callback'
scope = 'user-read-recently-played user-library-read user-top-read'

import requests
from datetime import datetime
from typing import List
import spotipy.util as util
from os import listdir
import warnings
warnings.filterwarnings("ignore")
client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def to_min_sec(milliseconds):
    seconds = milliseconds // 1000
    minutes = seconds // 60
    seconds = seconds % 60
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    return str(minutes) + ":" + str(seconds)
def get_album_name(album_id):
    metadata = sp.album(album_id)
    return metadata['name']
def get_album_pic(album_id):
    metadata = sp.album(album_id)
    return metadata['images'][1]['url']
def get_album_type(album_id):
    metadata = sp.album(album_id)
    ch=metadata['album_type']
    return ch[0].upper() + ch[1:]
def get_album_date(album_id):
    metadata = sp.album(album_id)
    return metadata['release_date']
def get_album_tracks(album_id):
    tracks = sp.album_tracks(album_id)
    stri=""
    for el in range(len(tracks['items'])):
        stri+=tracks["items"][el]['name']+" ("+to_min_sec(tracks["items"][el]['duration_ms'])+")/"
    return stri[:-2]

def get_genres(artist_id):
    metadata = sp.artist(artist_id)
    genres=metadata['genres']
    stri=""
    for el in genres:
        subel=el.split(" ")
        for s in subel:
            s=s[0].upper()+s[1:]
            if s[1:]==subel[-1][1:]:
                stri+=s+"/"
            else:
                stri+=s+" "
    return stri[:-1]
new=pd.read_csv("bij.csv")

#album_ids=new["album_id"].tolist()
art_ids=new["artist_id"].tolist()
"""
album_name=[]
album_type = []
album_date = []
album_tracks = []
album_pic = []
"""
genres = []
"""
for album_id in album_ids:
    album_name.append(get_album_name(album_id))

for album_id in album_ids:
    album_type.append(get_album_type(album_id))

for album_id in album_ids:
    album_date.append(get_album_date(album_id))
for album_id in album_ids:
    album_tracks.append(get_album_tracks(album_id))

for album_id in album_ids:
    album_pic.append(get_album_pic(album_id))
"""
for artist_id in art_ids:
    genres.append(get_genres(artist_id))


#new["album_name"]=album_name
#new["album_type"]=album_type
#new["album_date"]=album_date
#new["album_tracks"]=album_tracks
#new["album_pic"]=album_pic
new["genres"]=genres
new.to_csv("genred.csv",index=False)