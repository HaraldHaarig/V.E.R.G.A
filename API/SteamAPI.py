from steam_web_api import Steam
from decouple import config
import sys
from zmq import NULL
from API.GameAPI import getMoreDetails
#sys.path.insert(1, "C:\gitRepos\V.E.R.G.A")



def getSteamGamesbyID(id):

     #KEY=config("STEAM_API_KEY")
     steam=Steam("F113CBFAE50D9CD7BB8DE844BCFFE7C1")

     user=steam.users.get_user_details(id)

     response=steam.users.get_owned_games(user['player']['steamid'])
     
     

     count=response['game_count']
     web=[]
     names=[]
     


     #print(getMoreDetails("Minecraft")) # Placeholder for Spielbeschreibung

     for i in range(count):
          names.append(response['games'][i]['name'])
          
          game_id=response['games'][i]['appid']
          
          game_detail=steam.apps.get_app_details(game_id)
          
          if(game_detail[str(game_id)]['success']==True):
               web.append(game_detail[str(game_id)]['data']['header_image'])
          else:
               web.append(0)
     
     return web,names
    

