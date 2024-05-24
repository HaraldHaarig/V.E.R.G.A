import imp

from Tkinter_GUI.Spielcards import Spielcards
from Tkinter_GUI.Startseite import Startpage
from API.SteamAPI import getSteamGamesbyID
from Tkinter_GUI.Spielbeschreibung import spielbeschreibung_main
# Test_SteamID:76561199015522225 -> Sonrotz0815
from LoadingScreen import loadstartpage
from LoadingScreen import loadspielcards

# # generate classes


startpage = Startpage()

#lore = loadstartpage()
#lore = loadspielcards()


#test = Spielcards()

# url,title,details=getSteamGamesbyID("76561199015522225")


# count=0
# for s in url:
#     if s == 0:
#         url[count]="https://cdn-icons-png.flaticon.com/512/16/16096.png"
#     count+=1
# test.showallCards(url,title,details)
# test.showCard(url[0],title[0])


