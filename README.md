## Musical Time Machine
Go Back in Time: Enter a date, fetches Billboard Hot 100 songs, and creates a Spotify playlist for that day's top hits. Powered by web scraping using BeautifulSoup and Spotify API integration.

Create Spotify playlists for Billboard Hot 100 songs on a specific date!

## Description

This Python project allows users to input a date and generates a Spotify playlist containing the top songs from that day's Billboard Hot 100 chart. It uses web scraping to fetch song titles and the Spotify API to create playlists.

## Features

- Enter a date to retrieve Billboard Hot 100 songs.
- Automatically generates a Spotify playlist with the top songs.
- Uses web scraping to fetch song titles from Billboard's website.
- Integrates with Spotify API to create and populate playlists.

## Prerequisites

- Python 3.x installed on your system.
- Required Python packages: `requests`, `beautifulsoup4`.
- Spotify developer account and API credentials.
  
## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python packages using `pip`:
   `pip install -r requirements.txt`
3. Obtain Spotify API credentials and update the `spotify.py` file.

## Usage

1. Run the script:
  `python main.py`
2. Enter a date in the YYYY-MM-DD format.
3. Sit back and watch as the script generates a Spotify playlist!

## Acknowledgments

We acknowledge the invaluable contributions of the Spotify developer community and the Billboard website for providing the Hot 100 chart data.
