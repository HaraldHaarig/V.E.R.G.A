from Tkinter_GUI.Bibliothek import Bibliothek
from Tkinter_GUI.Spielcards import Spielcards
from API.SteamAPI import getSteamGamesbyID

from steam_web_api import Steam

steam=Steam("F113CBFAE50D9CD7BB8DE844BCFFE7C1")
# 105600
#print(steam.apps.get_app_details(105600))

# Test_SteamID:76561199015522225 -> Sonrotz0815


# generate classes
bibliothek = Bibliothek()

# test = Spielcards()


# # startpage = Startpage()




# url,title=getSteamGamesbyID("76561199015522225")


# # print(len(url), len(title) )
# count=0
# for s in url:
#     if s == 0:
#         url[count]="https://cdn-icons-png.flaticon.com/512/16/16096.png"
#     count+=1
# bibliothek.spielcards.showallCards(url,title)
# bibliothek.spielcards.showCard(url[0],title[0])