import requests
from dotenv import load_dotenv
import os
import webbrowser


load_dotenv(override=True)

rapid_key=os.getenv("RAPID_API_KEY")
raw_key=os.getenv("RAWG_API_KEY")


url = "https://rawg-video-games-database.p.rapidapi.com/games?key="+raw_key

headers = {
	"X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com",
    "X-RapidAPI-Key": rapid_key
}


print("Enter Gamen name: ")
game=input()
url+="&search_exact=true&search_precise=true&search="+game

response = requests.get(url, headers=headers)

data=response.json()

webbrowser.open(data['results'][0]['background_image']) 
#print(data['results'][1]['background_image'])
