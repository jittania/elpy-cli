"""
    Entry-point script for the whole program

    To run from command line:

    $ python -m elpy_cli
"""
import spotipy
import os
import sys
import json
import webbrowser
import spotipy.util as util
from dotenv import load_dotenv
from elpy_cli import __app_name__, __version__, spotipy_example, threading_stuff, printing_stuff
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyOAuth

# Loads environment variables from .env file (comparable to running `export ____` in terminal)
load_dotenv()

# Erase cache and prompt for user permission
def get_user_permission(username):
    try:
        token = util.prompt_for_user_token(username)
    except:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username)
    return token

def run_cli():
    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
    print("============================\n")
    print(f"{__app_name__} v{__version__}")
    print("\n============================\n")
    print("𓆏 ⊹☾⋆⁺₊🎧✩°｡ 𓆏 ⊹☾⋆⁺₊🎧✩°｡ 𓆏\n")
    print("\n*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")

    # input_username = input('What is your Spotify username?\n')
    # token = get_user_permission(input_username)
    token = get_user_permission('djsugrcut')
    spotify_obj = spotipy.Spotify(auth=token)

    # Get current user's display name:
    display_name = printing_stuff.get_current_user_display_name(spotify_obj)

    # Get audio features for a list of tracks:
    tracklist_audio_features = printing_stuff.get_several_track_audio_features(spotify_obj, ['3h5IIiL9vK5aR0DZO6jD7D', '79Dduf9L3DBCsmqgv5feXO', '65sELRQ2qrFIhtPaaSGyxu', '3983dFiS13NbeQcJzryFr4', '5X8kkUaUlAyAUr9TYqDFTH'])

    # Get most danceable track for list of tracks:
    most_danceable = printing_stuff.get_most_danceable_track(tracklist_audio_features)

    # ============================================================================

    print(f'✨ User: {display_name}\n')

    # print(json.dumps(tracklist_audio_features, sort_keys=True, indent=4))

    for track in tracklist_audio_features:
        track_details = spotify_obj.track(track['uri'], market=None)
        print(f"Track name: {track_details['name']}\n")
        print('Track features:')
        for audio_feature, value in track.items():
            print(f"  {audio_feature.capitalize()}: {value}")
        print('\n')
    
    print('💃 Most danceable track: ', spotify_obj.track(most_danceable, market=None)['name'])

    # Keep this - helpful, reusable line for printing json data in a readable way:
    # print(json.dumps(user_data, sort_keys=True, indent=4))


    
