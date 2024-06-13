from ctypes import sizeof
import requests
from dotenv import load_dotenv
import os
from zmq import NULL

def getMoreDetailsALL(gamename):
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
    
    try:
        if(data!=[] and data['results']!=[]):
            all_Platforms=[]

            for platforms in data['results'][0]['platforms']:
                all_Platforms.append(platforms['platform']['name'])

            return(data['results'][0]['released'], data['results'][0]['metacritic'], all_Platforms,data['results'][0]['description'],data['results'][0]['esrb_rating'][0]['name'])
        else:
            return NULL
    except KeyError:
        return NULL

def getMoreDetails(gamename):
    
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
    
    try:
        if(data!=[] and data['results']!=[]):
            all_Platforms=[]
            for platforms in data['results'][0]['platforms']:
                all_Platforms.append(platforms['platform']['name'])

            return(data['results'][0]['released'], data['results'][0]['metacritic'], all_Platforms)
        else:
            return NULL
    except KeyError:
        return NULL

def getImg(gamename):
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
    try:
        if(data!=[] and data['results']!=[]):
            return(data['results'][0]['background_image'])
        else:
            return 0
    except KeyError:
        return 0

def getAllGames(pages_anz):
    
    games=[]
    spareImg=[]
    details=[]
    load_dotenv(override=True)

    rapid_key=os.getenv("RAPID_API_KEY")
    raw_key=os.getenv("RAWG_API_KEY")

    url = "https://rawg-video-games-database.p.rapidapi.com/games?key="+raw_key

    headers = {
        "X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com",
        "X-RapidAPI-Key": rapid_key
    }
    count=0
    for pages in range(pages_anz):
        url+="&page="+str(pages+1)+"&page_size=40"
        response = requests.get(url, headers=headers)
        data=response.json()
        #print(data)
        for result in data['results']:
            count+=1
            games.append(result['name'])
            spareImg.append(result['background_image'])
            details.append(getMoreDetailsALL(result['name']))
    print(count)
    return games,spareImg,details