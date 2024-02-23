import requests
from dotenv import load_dotenv
import os
import json
import webbrowser


load_dotenv(override=True)

rapid_key=os.getenv("RAPID_API_KEY")
raw_key=os.getenv("RAWG_API_KEY")


url = "https://rawg-video-games-database.p.rapidapi.com/games?key="+raw_key+"&tags=multiplayer"

headers = {
	"X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com",
    "X-RapidAPI-Key": rapid_key
}

response = requests.get(url, headers=headers)

data=response.json()

# webbrowser.open(data['results'][1]['background_image']) The witcher background opens in browser
print(data['results'])
