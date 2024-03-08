from dotenv import load_dotenv
from steam import Steam
from decouple import config
from GameAPI import openWebGame
import sys
import os

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/Tkinter_GUI")

print("/".join(os.path.realpath(__file__).split("/")[0:-2])+"/Tkinter_GUI")



KEY=config("STEAM_API_KEY")
steam=Steam(KEY)


print("Enter SteamID: ")
id=input()

user=steam.users.get_user_details(id)
print(user)
# friendlist=steam.users.get_user_friends_list(user['player']['steamid'])
# print(friendlist)


response=steam.users.get_owned_games(user['player']['steamid'])
print(response)
count=response['game_count']
   

for i in range(count):
     #print(response['games'][i]['name'])
     web=openWebGame(response['games'][i]['name'])

createSpielcards(count,web)
