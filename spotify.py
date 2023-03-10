import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import pandas as pd

# export SPOTIPY_CLIENT_SECRET="4b2a58733e6a40c4b221d44d83f9d81a"
#export SPOTIPY_CLIENT_ID="ed6fe433e91b43a79490bea46ef85b00"
#export SPOTIPY_REDIRECT_URI="http://localhost:8000"

CLIENT_ID="ed6fe433e91b43a79490bea46ef85b00"
CLIENT_SECRET="4b2a58733e6a40c4b221d44d83f9d81a"

username = "reimuscendance"
scope = scope = "app-remote-control user-modify-playback-state streaming user-read-currently-playing user-read-playback-state"
redirect_uri = "http://localhost:8000"
token = util.prompt_for_user_token(username, scope, CLIENT_ID, CLIENT_SECRET, redirect_uri)
sp = spotipy.Spotify(auth=token)    
access_token = token



track_uri = "spotify:track:1BpKJw4RZxaFB88NE5uxXf"
sp.add_to_queue(track_uri)




artist_name = str(input("Please Enter the artists name you want to see"))

results = sp.search(q=artist_name, type='artist')
items = results['artists']['items']

if len(items) > 0:
    artist = items[0]
    print(f"Artist: {artist['name']}")
    print(f"URI: {artist['uri']}")
else:
    print(f"No artist found with name '{artist_name}'.")


results = sp.artist_top_tracks((f"{artist['uri']}"))

user_choice = int(input("How many top songs do you want to see? "))

for track in results['tracks'][:user_choice]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()


    
