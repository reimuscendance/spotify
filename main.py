import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import pandas as pd
import json
import matplotlib.pyplot as plt

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

def request(endpoint: str) -> dict:
    resp = requests.get(
        "https://api.spotify.com/v1/" + endpoint,
        headers={'Authorization': 'Bearer ' + token}
    )

    resp.raise_for_status()
    return resp.json()

def artist_search():
    artist_name = input("Please Enter the artists name you want to see")


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


def song_search():
    # Search for the artist
    search_query = input("Please Enter the song you want to see: ")
    response_json = request(f'search?q={search_query}&type=track')

    # Get the URI
    track_uri = response_json['tracks']['items'][0]['uri']
    print(track_uri)

    # Get the name
    sp.add_to_queue(track_uri)
    sp.next_track()
    sp.start_playback()
    
def data_panda():
    search_query = input("Please Enter the song you want to see: ")
    response_json = request(f'search?q={search_query}&type=track')

    # Get the URI
    track_id = response_json['tracks']['items'][0]['id']
    resp_json = request('audio-features/' + track_id)
    print(pd.json_normalize(resp_json))


menu = input("Please select an option:\n1. Search for an artist\n2. Search for a song\n3.Graph for song\n")
if menu == "1":
    artist_search()
if menu == "2":
    song_search()
elif menu == "3":
    data_panda()
elif menu == "5":
    pass