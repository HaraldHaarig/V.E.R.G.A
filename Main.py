from Tkinter_GUI.Spielcards import Spielcards
from API.SteamAPI import getSteamGamesbyID
# Test_SteamID:76561199015522225 -> Sonrotz0815


# Testing Spielcards
test = Spielcards()

url,title=getSteamGamesbyID("76561199015522225")

# print(len(url), len(title) )
count=0
for s in url:
    if s == 0:
        url[count]="https://cdn-icons-png.flaticon.com/512/16/16096.png"
    count+=1
test.showallCards(url,title)
# test.showCard(url[0],title[0])