import requests
from dotenv import load_dotenv
import os
from zmq import NULL

def openWebGame(gamename):
    
    load_dotenv(override=True)

    rapid_key=os.getenv("RAPID_API_KEY")
    raw_key=os.getenv("RAWG_API_KEY")

    url = "https://rawg-video-games-database.p.rapidapi.com/games?key="+raw_key

    headers = {
        "X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com",
        "X-RapidAPI-Key": rapid_key
    }
    url+="&search_exact=true&search_precise=true&search="+gamename
    response = requests.get(url, headers=headers)
    data=response.json()
    if(data['results']!=[]):
        return(data['results'][0]['background_image'])
    else:
        return NULL

 
