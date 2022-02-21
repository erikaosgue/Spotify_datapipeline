"""
Get playlist data from a scpefic user of spotify
"""
import random
from producer import producer_func
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import time
import signal
import sys

load_dotenv()
CLIENT_ID=os.environ["CLIENT_ID"]
SECRET_ID=os.environ.get("SECRET_ID")

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=SECRET_ID)
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_playlist(user='spotify'):
    """
    Get the playlist from a specific user 
    """
    playlists = sp.user_playlists(user)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            playlist_dict = {
                'playlists_offset': i + 1 + playlists['offset'],
                'playlist_name': playlist['name'],
                'playlist_uri':  playlist['uri']
                }
            producer_func(playlist_dict)
            time_to_sleep = random.randint(1, 11)
            time.sleep(time_to_sleep)
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

def signal_handler(sig, frame):
    """
    Handler to catch the CRTL+C keyword to stop the program
    """
    print('\n= BYE! =')
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler) 
    get_playlist()
