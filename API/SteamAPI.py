from steam import Steam
from decouple import config
import sys

from zmq import NULL
from API.GameAPI import openWebGame
sys.path.insert(1, "C:\gitRepos\V.E.R.G.A")



def getSteamGamesbyID(id):

     KEY=config("STEAM_API_KEY")
     steam=Steam(KEY)

     user=steam.users.get_user_details(id)

     response=steam.users.get_owned_games(user['player']['steamid'])
     
     count=response['game_count']
     web=[]
     names=[]
     
     for i in range(count):
          names.append(response['games'][i]['name'])
          games=steam.apps.search_games(response['games'][i]['name'])
          if(games['apps'] != []):
               #web.append(openWebGame(response['games'][i]['name']))
               web.append(games['apps'][0]['img'])
          else:
               web.append(0)
     
     return web,names
    

