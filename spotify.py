import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "4ff8970ec2d94fe9b2aef8d5c42376c2"
SPOTIFY_CLIENT_SECRET = "51713c8dce644f8088aaf86441ed428a"


class Spotipy:
    """
        A class to interact with the Spotify API for searching tracks, creating playlists, and adding songs to playlists.

        Attributes:
            song_uris (list): A list to store Spotify track URIs.
            year (int): The year to filter track searches.

        Methods:
            search_tracks(song_list):
                Search for tracks on Spotify based on a list of song titles.
                Returns a list of track URIs found on Spotify.

            create_playlist(name):
                Create a private playlist for the authenticated user.
                Returns the ID of the created playlist.

            add_songs_to_playlist(playlist_id, songs):
                Add a list of songs to a specified playlist by their track URIs.
    """

    def __init__(self, year: int):
        """
            Initialize Spotipy object with a specific year and set up Spotify authentication.

            Args:
                year (int): The year to filter track searches.
        """

        self.song_uris = None
        self.year = year
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                                            client_secret=SPOTIFY_CLIENT_SECRET,
                                                            redirect_uri="https://open.spotify.com/",
                                                            scope="user-library-read playlist-modify-private",
                                                            show_dialog=True,
                                                            cache_path="token.txt",
                                                            ))

    def search_tracks(self, song_list: list) -> list:
        """
            Search for tracks on Spotify based on a list of song titles.

            Args:
                song_list (list): A list of song titles to search for.
            Returns:
                list: A list of track URIs found on Spotify.
        """
        self.song_uris = []
        for song in song_list:
            results = self.sp.search(q=f"track:{song}", type="track")
            try:
                uri = results["tracks"]["items"][0]["uri"]
                self.song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
        return self.song_uris

    def create_playlist(self, name: str) -> int:
        """
            Create a private playlist for the authenticated user.

            Args:
                name (str): The name of the playlist.
            Returns:
                str: The ID of the created playlist.
        """

        user_id = self.sp.current_user()["id"]
        playlist = self.sp.user_playlist_create(user=user_id, name=name, public=False, collaborative=False)
        playlist_id = playlist["id"]
        return playlist_id

    def add_songs_to_playlist(self, playlist_id: int, songs: list) -> None:
        """
            Add a list of songs to a specified playlist by their track URIs.

            Args:
                playlist_id (int): The ID of the playlist.
                songs (list): A list of track URIs to add to the playlist.
            Returns:
                None
        """

        self.sp.playlist_add_items(playlist_id, songs, position=None)
