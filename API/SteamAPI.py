from dotenv import load_dotenv
from steam import Steam
from decouple import config
from zmq import NULL

import sys
import os

sys.path.insert(1, "C:\gitRepos\V.E.R.G.A")
# from Tkinter_GUI.Spielcards import createSpielcards
from API.GameAPI import openWebGame



def getSteamGamesbyID(id):



     KEY=config("STEAM_API_KEY")
     steam=Steam(KEY)

     user=steam.users.get_user_details(id)

     response=steam.users.get_owned_games(user['player']['steamid'])
     
     

     count=response['game_count']
     web=[]

     for i in range(count):
          #print(temp)
          games=steam.apps.search_games(response['games'][i]['name'])
          if games['apps']!=[]:
               web.append(games['apps'][0]['img'])
    # createSpielcards(web)

