"""
    Lil test scripty for getting Spotipy authentication working
    From https://spotipy.readthedocs.io/en/2.24.0/#
    "Here is an example of using Spotipy to list the names of all the 
    albums released by the artist ‘Birdy’:"
"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def spotipy_example_call():
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])