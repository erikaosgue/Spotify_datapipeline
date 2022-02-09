"""
Get playlist data from a scpefic user of spotify
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID=os.environ["client_id"]
SECRET_ID=os.environ.get("client_secret")


auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=SECRET_ID)
sp = spotipy.Spotify(auth_manager=auth_manager)


def get_playlist(user='spotify'):

    playlists = sp.user_playlists(user)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%4d playlist_uri: %s playlist_name: %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None



if __name__ == "__main__":
    get_playlist()
