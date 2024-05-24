from numpy import size
from steam import Steam
from decouple import config
import sys

from sympy import det
from zmq import NULL
from API.GameAPI import getMoreDetails
from API.GameAPI import getAllGames
from API.GameAPI import getImg
sys.path.insert(1, "C:\gitRepos\V.E.R.G.A")



def getSteamGamesbyID(id):

     
     KEY=config("STEAM_API_KEY")
     steam=Steam(KEY)

     try:
          int(id)
     except ValueError:
          id=steam.users.get_steamid(id)

     user=steam.users.get_user_details(id)
     
     response=steam.users.get_owned_games(user['player']['steamid'])
     
     
     try:
          count=response['game_count']
     except KeyError:
          print("Attention:Steam Account must be public !")
     web=[]
     names=[]
     details=[[0 for x in range(9)] for y in range(count)] 
     #details=getMoreDetails("Minecraft") # Placeholder for Spielbeschreibung

     for i in range(count):
          
          names.append(response['games'][i]['name'])
          temp=getMoreDetails(names[i])
          
          if(temp!=0):
            details[i][5]=temp[0]
            details[i][6]=temp[1]
            details[i][7]=temp[2]
          
          temp=response['games'][i]['name']
          temp1=steam.apps.search_games(temp)
          
          if(temp1["apps"]!=[]):
               details[i][0]=temp1["apps"][0]['price']
          
          
          details[i][1]=response['games'][i]['playtime_forever']


          game_id=response['games'][i]['appid']
          
          game_detail=steam.apps.get_app_details(game_id)
          
          if(game_detail[str(game_id)]['success']==True):
               
               web.append(game_detail[str(game_id)]['data']['header_image'])
               details[i][2]=game_detail[str(game_id)]['data']['short_description']
               details[i][3]=game_detail[str(game_id)]['data']['required_age']
               try:
                    details[i][4]=game_detail[str(game_id)]['data']['controller_support']
               except KeyError:
                    details[i][4]="UNKNOWN"

          else:
               web.append(0)
          print(details)


     
     return web,names,details
    



