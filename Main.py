from Tkinter_GUI.Spielcards import Spielcards
from API.SteamAPI import getSteamGamesbyID
# Test_SteamID:76561199015522225 -> Sonrotz0815


# Testing Spielcards
test = Spielcards()

url,title=getSteamGamesbyID("76561199015522225")

test.showCard(url[0],title[0])