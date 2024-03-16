from steam import Steam
from decouple import config
import sys
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
          games=openWebGame(names[i])
          web.append(games)
          

     return web,names
    

