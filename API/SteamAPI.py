from dotenv import load_dotenv
from steam import Steam
from decouple import config
from zmq import NULL

import sys
import os

sys.path.insert(1, "C:\gitRepos\V.E.R.G.A")
from Tkinter_GUI.Spielcards import createSpielcards
from API.GameAPI import openWebGame



def getSteamGamesbyID(id):



     KEY=config("STEAM_API_KEY")
     steam=Steam(KEY)

     user=steam.users.get_user_details(id)

     response=steam.users.get_owned_games(user['player']['steamid'])

     count=response['game_count']
     counter=0
     web=[]   

     for i in range(count):
          temp=openWebGame(response['games'][i]['name'])
          if(temp != NULL):
               web.append(temp)

     createSpielcards(count,web)
