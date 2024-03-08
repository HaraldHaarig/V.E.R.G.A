import requests
from dotenv import load_dotenv
import os
from steam import Steam
from decouple import config
import webbrowser
from GameAPI import openWebGame

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
     print(response['games'][i]['name'])
     openWebGame(response['games'][i]['name'])
    