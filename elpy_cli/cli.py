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

    input_username = input('What is your Spotify username?\n')
    token = get_user_permission(input_username)

    spotify_obj = spotipy.Spotify(auth=token)


    
