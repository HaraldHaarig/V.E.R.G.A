from uu import Error
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
            url=f"https://api.rawg.io/api/games/{data['results'][0]['id']}?key="+raw_key
            response=requests.get(url, headers=headers)
            try:
                dataid=response.json()
                controllersupport="No Controller Support"
                for i in range(len(dataid['tags'])):
                    if(dataid['tags'][i]['name']=="Full controller support"):
                        controllersupport=dataid['tags'][i]['name']
            except Error:
                print("Error")
            
            try:
                ageRating=data['results'][0]['esrb_rating']['name']
            except TypeError:
                ageRating="NAN"
            for platforms in data['results'][0]['platforms']:
                all_Platforms.append(platforms['platform']['name'])

            return(data['results'][0]['released'], data['results'][0]['metacritic'], all_Platforms, ageRating, dataid['description'], controllersupport)
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
        try:
            for result in data['results']:
                count+=1
                games.append(result['name'])
                spareImg.append(result['background_image'])
                details.append(getMoreDetailsALL(result['name']))
        except KeyError:
            print("Error")
    print(count)
    return games,spareImg,details

def getGame(title):
    load_dotenv(override=True)

    rapid_key=os.getenv("RAPID_API_KEY")
    raw_key=os.getenv("RAWG_API_KEY")

    url = "https://rawg-video-games-database.p.rapidapi.com/games?key="+raw_key

    headers = {
        "X-RapidAPI-Host": "rawg-video-games-database.p.rapidapi.com",
        "X-RapidAPI-Key": rapid_key
    }
    url+="&search_exact=true&search_precise=true&search="+title
    response = requests.get(url, headers=headers)
    data=response.json()


    img=data['results'][0]['background_image']
    details=getMoreDetailsALL(data['results'][0]['name'])    
    return img,details