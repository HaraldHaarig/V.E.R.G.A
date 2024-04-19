from steam import Steam
from decouple import config
import sys

from sympy import det
from zmq import NULL
from API.GameAPI import getMoreDetails
sys.path.insert(1, "C:\gitRepos\V.E.R.G.A")



def getSteamGamesbyID(id):

     KEY=config("STEAM_API_KEY")
     steam=Steam(KEY)

     user=steam.users.get_user_details(id)

     response=steam.users.get_owned_games(user['player']['steamid'])
     
     

     count=response['game_count']
     web=[]
     names=[]
     details=[[0]*(5)]*count
     #details=getMoreDetails("Minecraft") # Placeholder for Spielbeschreibung

     for i in range(count):
          names.append(response['games'][i]['name'])
          temp=response['games'][i]['name']
          temp1=steam.apps.search_games(temp)
          
          if(temp1["apps"]!=[]):
               details[i][0]=temp1["apps"][0]['price']
          
          
          details[i][1]=response['games'][i]['playtime_forever']


          game_id=response['games'][i]['appid']
          
          game_detail=steam.apps.get_app_details(game_id)
          
          if(game_detail[str(game_id)]['success']==True):
               
               web.append(game_detail[str(game_id)]['data']['header_image'])
               details[i][2]=game_detail[str(game_id)]['data']['detailed_description']
               details[i][3]=game_detail[str(game_id)]['data']['required_age']
               try:
                    details[i][4]=game_detail[str(game_id)]['data']['controller_support']
               except KeyError:
                    details[i][4]="UNKNOWN"

          else:
               web.append(0)
     
     return web,names,details
    

