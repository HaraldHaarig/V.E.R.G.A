import requests
from dotenv import load_dotenv
import os
from urllib.parse import urlencode


load_dotenv(override=True)

def get_summoner_info(summoner_name=None,tag=None):
    # if not summoner_name:
    #     summoner_name = input("Summoner Name: ")
    api_key=os.getenv("RIOT_API_KEY")
    params={
        'api_key':api_key
    }
    api_url=f"https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag}?api_key={api_key}"

    
    response=requests.get(api_url, params=urlencode(params))
    response.raise_for_status()
    return response.json()
    # except requests.exceptions.RequestException as e:
    #     print("API sagt nein: {e}")
    #     return None