import requests
from validate_date import ValidateDate
from spotify import Spotipy
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"


# ------------------------------ Ask the user for a valid date in the YYYY-MM-DD format ------------------------------ #
valid_date = False
date = ''
while not valid_date:
    date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ")
    validate_date = ValidateDate(date)  # Create an instance of ValidateDate class
    if validate_date.validate_date():   # Validate the entered date
        valid_date = True

# ----------------------------- Fetch the Billboard Hot 100 songs for the specified date ----------------------------- #
response = requests.get(f"{BILLBOARD_URL}{date}")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# Extract the titles of the top 100 songs
top_100 = soup.find_all(name='h3', class_='a-no-trucate')
top_100_titles = [song.get_text().strip() for song in top_100]
print(top_100_titles)


# ---------------------- Initialize Spotipy object using the year extracted from the input date ---------------------- #

spotify = Spotipy(int(date.split('-')[0]))

# Search for Spotify track URIs for the Billboard Hot 100 songs
SongUris = spotify.search_tracks(top_100_titles)
print(SongUris)

# Create a playlist on Spotify named with the date and add the songs to it
playlist_name = f"{date}: BILLBOARD-100"
playlist_id = spotify.create_playlist(playlist_name)
spotify.add_songs_to_playlist(playlist_id, SongUris)
