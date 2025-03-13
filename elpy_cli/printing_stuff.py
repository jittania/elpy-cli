""" Here is what the SpotifyOAuth class needs to authenticate requests (using the "Authorization Code Flow," not the "Client Credentials flow" - note that the latter offers higher rate limiting, but any endpoints that access user information require the former)

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_APP_CLIENT_ID",
                                               client_secret="YOUR_APP_CLIENT_SECRET",
                                               redirect_uri="YOUR_APP_REDIRECT_URI",
                                               scope="user-library-read"))

"""
import spotipy
import os
import sys
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyOAuth


def get_current_user_display_name(spotify_obj):
    user = spotify_obj.current_user()
    return user["display_name"]

def get_several_track_audio_features(spotify_obj, track_uris):
    # How to get track URIs: https://community.spotify.com/t5/FAQs/Basics-of-a-Spotify-URL/ta-p/919201#:~:text=Answer%3A,or%20Artist%20Profile%20on%20Spotify. 
    
    tracklist_audio_features = spotify_obj.audio_features(tracks=track_uris)
    return tracklist_audio_features

def get_most_danceable_track(tracklist_audio_features):
    """ assumes tracks will have unique danceability ratings """
    max = 0
    most_danceable_track_uri = ''
    for track in tracklist_audio_features:
        track_danceability = track['danceability']
        if track_danceability > max:
            max = track_danceability
            most_danceable_track_uri = track['uri']
    return most_danceable_track_uri
    

def get_track_audio_analysis():
    pass

def get_playlist_genres_from_artists():
    pass

def write_playlist_description():
    pass

    # get user conf on overwriting description text